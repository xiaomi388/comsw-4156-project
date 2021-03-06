from flask import Flask, request
import furniture
import search
import user
import profile
import db
from flask_login import LoginManager, login_required, \
    login_user, logout_user, current_user
from flask_cors import CORS

db.init_db()
app = Flask(__name__)
login_manager = LoginManager()
login_manager.login_view = "/user/login"
login_manager.session_protection = None
app.secret_key = '4156'
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="None"
)
CORS(app, supports_credentials=True)
login_manager.init_app(app)


@app.route("/furnitures", methods=["POST"])
@login_required
def post_furniture():
    return furniture.create_furniture(
        request.get_json(), current_user.get_email())


@app.route("/furniture", methods=["GET"])
def search_furniture():
    keyword = request.args.get('keyword')
    res = search.search_furniture(keyword)
    return res


@app.route("/user/login", methods=["POST"])
def user_login():
    resp, status_code, user_login_obj = user.user_login(request.form)
    if status_code == 200:
        login_user(user_login_obj)
        # resp.headers.add("Access-Control-Allow-Headers", "*")
        # resp.headers.add("Access-Control-Expose-Headers", "*")
        # resp.headers.add("hello", "1244")
    return resp, status_code


@login_manager.user_loader
def load_user(user_id):
    return user.UserLoginObj.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return user.need_login_response()


@app.route('/user/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    return user.user_logout_resp()


@app.route("/register", methods=["POST"])
def user_register():
    return user.register(request.form)


@app.route("/profile", methods=["GET"])
@login_required
def get_profile():
    # user_email = request.args.get('email')
    res = profile.get_profile(current_user.get_email())
    return res


@app.route("/furnitures/<fid>/rate", methods=["POST"])
@login_required
def post_rate(fid):
    rating = request.args.get('rating', type=int)
    return furniture.rate_owner(fid, current_user.get_email(), rating)


@app.route("/furnitures/<fid>/buy", methods=["POST"])
@login_required
def buy_furniture(fid):
    return furniture.buy_furniture(fid, current_user.get_email())


@app.route("/furnitures/<fid>/confirm", methods=["POST"])
@login_required
def owner_confirm(fid):
    is_confirm = request.args.get('confirm')
    print(is_confirm)
    return furniture.owner_confirm(fid, current_user.get_email(), is_confirm)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
