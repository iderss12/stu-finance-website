import os
from flask import Flask, render_template, redirect, url_for, request


static = os.path.join(os.path.dirname(__file__), "static")
app = Flask(
    __name__, static_url_path="", static_folder="static", template_folder="templates"
)


@app.route("/")
def toIndex():
    return redirect(url_for("index"))


@app.route("/index.html")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
