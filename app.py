from flask import Flask, request
import furniture
import search
import user
import profile
import db
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

db.init_db()
app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/user/login"
app.secret_key = '4156'


@app.route("/furnitures", methods=["POST"])
@login_required
def post_furniture():
    return furniture.create_furniture(request.get_json(), current_user.get_email())


@app.route("/furniture", methods=["GET"])
def search_furniture():
    keyword = request.args.get('keyword')
    res = search.search_furniture(keyword)
    return res


@app.route("/user/login", methods=["GET"])
def user_login():
    email = request.args.get("email")
    password = request.args.get("password")
    resp, status_code, user_login_obj = user.user_login(email, password)
    if status_code == 200:
        login_user(user_login_obj)
    return resp, status_code


@login_manager.user_loader
def load_user(user_id):
    return user.UserLoginObj.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
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


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
