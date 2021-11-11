import jsonschema
import json
import sqlite3


def create_furniture(req):
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
        jsonschema.validate(instance=req, schema=schema)
    except (ValueError, jsonschema.exceptions.ValidationError):
        return json.dumps({"error": "input invalid."}), 400
    # FIXME: use real user id
    req["owner"] = "mockuser"

    # write into db
    try:
        conn = sqlite3.connect("sqlite_db")
        stmt = (
            "INSERT INTO Furniture "
            "(owner, title, labels, image_url, description) "
            "VALUES (?, ?, ?, ?, ?)"
        )
        conn.execute(
            stmt, [req[k] for k in ["owner", "title",
                                    "labels", "image_url",
                                    "description"]]
        )
        conn.commit()
    except sqlite3.Error as e:
        return json.dumps({"error": f"db error: {str(e)}"}), 500
    return json.dumps({"error": ""}), 201
