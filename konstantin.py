from flask import Blueprint, render_template, redirect
import storage

konstantin = Blueprint("konstantin", __name__)


@konstantin.route("/list")
def show_list():
    return render_template(
        "list.html",
        requests=storage.requests
    )


@konstantin.route("/view/<int:id>")
def view_request(id):
    item = next(
        (x for x in storage.requests if x["id"] == id),
        None
    )

    if item is None:
        return "Заявка не найдена", 404

    return render_template("view.html", item=item)


@konstantin.route("/delete/<int:id>", methods=["POST"])
def delete_request(id):
    storage.requests[:] = [
        x for x in storage.requests if x["id"] != id
    ]

    return redirect("/list")