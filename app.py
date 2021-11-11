from flask import Flask, request
import furniture

app = Flask(__name__)


@app.route("/furnitures", methods=["POST"])
def post_furniture():
    return furniture.create_furniture(request.get_json())
