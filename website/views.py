from flask import Blueprint, render_template, redirect, url_for, request

views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def toIndex():
    return redirect(url_for("views.index", lang="mn"))


@views.route("/<lang>/index.html", methods=["GET"])
def index(lang):
    return render_template("/" + lang + "/index.html")


# @views.route("/<lang>/about.html", methods=["GET", "POST"])
# def about(lang):
#     return render_template("/" + lang + "/about.html")
