
from flask import Flask, render_template
from anton import anton
from konstantin import konstantin

app = Flask(__name__)

app.register_blueprint(anton)
app.register_blueprint(konstantin)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
