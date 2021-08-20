from flask import Flask, jsonify
from api import get_lenovo

app = Flask(__name__)


@app.route("/")
def get_laptops():
    laptops = get_lenovo()
    return jsonify(laptops)
