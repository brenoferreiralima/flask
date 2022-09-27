from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact")
def contatos():
    return render_template("contact.html")


@app.route("/user/<user_name>")
def user(user_name):
    return render_template("user.html")


if __name__ == "__main__":
    app.run(debug=True)