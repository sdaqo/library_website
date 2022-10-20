from flask import Blueprint, session, redirect

misc_bluep = Blueprint("misc_bluep", __name__, template_folder="templates")


@misc_bluep.route("/darkmode", methods=["GET"])
def toggle_darkmode():
    darkmode = session.get("darkmode", False)
    session["darkmode"] = not darkmode

    return redirect(request.args.get("ref", "/"))