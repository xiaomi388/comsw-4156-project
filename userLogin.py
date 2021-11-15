import jsonschema
import json
import flask
import sqlite3
import userDB

def set_user_cookie(email:str, resp):
    resp.set_cookie('user', email)

def need_login_response():
    return json.dumps({"error": f"Please login first"}), 400

def user_login(req):
    # integrity check
    print(req.endpoint)
    try:
        email = req.args.get("email")
        password = req.args.get("password")
        print(email, password)
        saved_user = userDB.select_user_by_email(email)
        print(saved_user)
        if not saved_user:
            return json.dumps({"error": f"No such email {str(email)}"}), 400
        # To Do: md5
        if not password == saved_user.get_password():
            return json.dumps({"error": f"wrong password {str(email)}"}), 400
        resp = flask.make_response(json.dumps({"error": ""}))
        set_user_cookie(email, resp)
        return resp, 200
    except :
        return json.dumps({"error": f"Internal error"}), 500

