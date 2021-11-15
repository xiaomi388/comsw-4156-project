import json
import sqlite3


def get_profile(email):
    if email is None:
        return json.dumps({"error": "email is empty"}), 400
    conn = None
    try:
        conn = sqlite3.connect("sqlite_db")
        search_profile_res = conn.execute("SELECT * FROM USER WHERE email=?",
                                          [email]).fetchall()
        conn.commit()
        if len(search_profile_res) == 0:
            return json.dumps({"error": "no matched user profile found"}), 201
        for p in search_profile_res:
            email, password, name, zipcode, rating, \
                transcation_count, phone_number = p
            profile_info = {"email": email, "name": name, "zipcode": zipcode,
                            "phone_number": phone_number}
        return json.dumps({"profile": profile_info})
    except sqlite3.Error as e:
        return json.dumps({"error": f"db error: {str(e)}"}), 500
    finally:
        if conn:
            conn.close()
