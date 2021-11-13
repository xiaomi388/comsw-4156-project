from flask import Flask, request
import furniture
import search
import user

app = Flask(__name__)


@app.route("/furnitures", methods=["POST"])
def post_furniture():
    return furniture.create_furniture(request.get_json())


@app.route("/furniture", methods=["GET"])
def search_furniture():
    keyword = request.args.get('keyword')
    res = search.search_furniture(keyword)
    return res


@app.route("/register", methods=["POST"])
def user_register():
    return user.register(request.form)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
