 from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    # Load boy.html instead of login.html
    return render_template("boy.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Replace with your own logic or database check
    if username == "admin" and password == "secret123":
        return render_template("success.html", username=username)
    else:
        return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)