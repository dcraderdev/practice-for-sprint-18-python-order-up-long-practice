from flask import Blueprint, render_template
from flask_login import login_required


bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/orders")
@login_required
def index():
    # return "Order Up!"
    return render_template('orders.html')


# @bp.route("/halp", methods=["GET", "POST"])
# def halp():
#   return '<h1>Home</h1>'    