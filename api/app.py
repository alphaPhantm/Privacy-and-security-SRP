from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("landingpage.html")

@app.route("/calculate", methods=["POST", "GET"])
def calculate():

    return render_template("result.html")



if __name__ == '__main__':
    app.run(port=1337, debug=True)
