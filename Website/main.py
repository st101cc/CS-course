from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/source")
def source():
    return render_template("source.html")

@app.route("/clean")
def clean():
    return render_template("clean.html")

@app.route("/visual")
def visual():
    return render_template("visual.html")

if __name__ == "__main__":
    app.run(debug=True)



