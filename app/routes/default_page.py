from flask import Blueprint, render_template

default_bp = Blueprint('default', __name__)

@default_bp.route('/')
def default():
    return render_template("default_page/default_page.html")