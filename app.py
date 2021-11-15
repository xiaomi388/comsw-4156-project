from flask import Flask, request
import furniture
import search
import user
import profile


app = Flask(__name__)

user_email = None

@app.route("/furnitures", methods=["POST"])
def post_furniture():
    return furniture.create_furniture(request.get_json(), user_email)


@app.route("/furniture", methods=["GET"])
def search_furniture():
    keyword = request.args.get('keyword')
    res = search.search_furniture(keyword)
    return res



@app.route("/user/login", methods=["GET"])
def user_login():
    return user.user_login(request)


@app.before_request
def get_user_email():
    if str(request.url_rule) not in ["/user/login", "/register"]:
        global user_email
        # print("last email", user_email)
        # print("cookie is ", request.cookies.get('user'))
        user_email = request.cookies.get('user')
        if not user_email:
            return user.need_login_response()
        else:
            print(f"get user cookie {user_email}")

@app.route("/register", methods=["POST"])
def user_register():
    return user.register(request.form)

@app.route("/profile", methods=["GET"])
def get_profile():
    user_email = request.args.get('email')
    res = profile.get_profile(user_email)
    return res



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
