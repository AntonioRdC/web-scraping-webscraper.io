from flask import Flask, render_template
from api import get_lenovo

app = Flask(__name__)


@app.route("/")
def get_laptops(laptops=None):
    laptops = get_lenovo()
    return render_template('index.html', laptops=laptops)
