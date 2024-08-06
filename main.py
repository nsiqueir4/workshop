from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/inscricoes")
def login():
    return render_template("inscrições.html")

if __name__ == "__main__":
    app.run()