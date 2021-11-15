import json
import sqlite3


def search_furniture(keyword):
    if keyword is None:
        return json.dumps({"error": "keyword is empty"}), 400
    conn = None
    try:
        conn = sqlite3.connect("sqlite_db")
        search_label_res = conn.execute("SELECT * FROM \
                                         Furniture WHERE labels=?",
                                        [keyword]).fetchall()
        conn.commit()
        if len(search_label_res) == 0:
            return json.dumps({"error": "no matched furniture found"}), 201
        furniture_list = []
        for f in search_label_res:
            fid, owner, title, labels, status, image_url, description = f
            furniture_list.append({"fid": fid, "owner": owner,
                                   "title": title, "labels": labels,
                                   "status": status, "image_url": image_url,
                                   "description": description})
        return json.dumps({"furniture": furniture_list})
    except sqlite3.Error as e:
        return json.dumps({"error": f"db error: {str(e)}"}), 500
    finally:
        if conn:
            conn.close()
