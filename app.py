from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet")
def greet():
    name = request.args.get("name", "world")
    return render_template("greet.html", name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # This line can be removed when using Gunicorn