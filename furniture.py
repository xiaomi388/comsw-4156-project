import jsonschema
import json
import sqlite3


def create_furniture(furniture, owner):
    """ used by user to post a new furniture

    :param furniture: a json object representing a furniture
    :return: (response body, status code)
    """
    # integrity check
    schema = {
        "type": "object",
        "required": ["title", "labels", "image_url", "description"],
        "properties": {
            "title": {"type": "string"},
            "labels": {"type": "string"},
            "image_url": {"type": "string"},
            "description": {"type": "string"},
        }
    }
    try:
        jsonschema.validate(instance=furniture, schema=schema)
    except (ValueError, jsonschema.exceptions.ValidationError):
        return json.dumps({"error": "input invalid."}), 400
    furniture["owner"] = owner

    # write into db
    conn = None
    try:
        conn = sqlite3.connect("sqlite_db")
        stmt = (
            "INSERT INTO Furniture "
            "(owner, title, labels, image_url, description) "
            "VALUES (?, ?, ?, ?, ?)"
        )
        conn.execute(
            stmt, [furniture[k] for k in ["owner", "title",
                                          "labels", "image_url",
                                          "description"]]
        )
        conn.commit()
    except sqlite3.Error as e:
        return json.dumps({"error": f"db error: {str(e)}"}), 500
    finally:
        if conn:
            conn.close()
    return json.dumps({"error": ""}), 201


def rate_owner(fid, buyer_email, rating):
    if not (0 <= rating <= 5):
        return json.dumps(
            {"error": "rating score should be in the range of [0, 5]"}), 400
    conn = None
    try:
        conn = sqlite3.connect("sqlite_db")
        record = conn.execute(
            "SELECT buyer, owner, status FROM Furniture WHERE fid = ?",
            [fid]
        ).fetchone()
        if record is None:
            return json.dumps({"error": "fid not existed"}), 400
        real_buyer_email, owner, status = record
        if buyer_email != real_buyer_email:
            return json.dumps(
                {"error": "rating can only be triggered by the buyer"}), 400
        if status == "rated":
            return json.dumps(
                {"error": "this transaction has been rated"}), 400
        if status != "completed":
            return json.dumps(
                {"error": "please rate after the transaction is completed"}
            ), 400
        conn.execute(
            "UPDATE user SET transaction_count = "
            "transaction_count+1, rating = rating+?"
            "WHERE email = ?",
            [rating, owner]
        )
        conn.execute(
            "UPDATE furniture SET status = 'rated' WHERE fid=?",
            [fid]
        )
        conn.commit()
    except sqlite3.Error as e:
        return json.dumps({"error": f"db error: {str(e)}"}), 500
    finally:
        if conn:
            conn.close()
    return json.dumps({"error": ""}), 200
