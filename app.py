from flask import Flask, render_template
from gradio_client import Client, handle_file
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

