import jsonschema
import json
import sqlite3


def create_furniture(furniture):
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
    # FIXME: use real user id
    furniture["owner"] = "mockuser"

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
