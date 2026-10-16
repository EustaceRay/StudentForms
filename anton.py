
from flask import Blueprint, render_template, request, redirect
import storage

anton = Blueprint("anton", __name__)


@anton.route("/new", methods=["GET", "POST"])
def new_request():
    if request.method == "POST":
        item = {
            "id": storage.next_id,
            "name": request.form["name"],
            "description": request.form["description"],
            "category": request.form["category"],
            "priority": request.form["priority"]
        }

        storage.requests.append(item)
        storage.next_id += 1

        return redirect("/list")

    return render_template("form.html", item=None)


@anton.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_request(id):
    item = next(
        (x for x in storage.requests if x["id"] == id),
        None
    )

    if item is None:
        return "Заявка не найдена", 404

    if request.method == "POST":
        item["name"] = request.form["name"]
        item["description"] = request.form["description"]
        item["category"] = request.form["category"]
        item["priority"] = request.form["priority"]

        return redirect("/list")

    return render_template("form.html", item=item)
