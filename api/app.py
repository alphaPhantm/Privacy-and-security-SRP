from flask import Flask, render_template, request
import control

app = Flask(__name__)

app.template_folder = "../templates"
app.static_folder = "../static"

@app.route("/")
def index():
    return render_template("landingpage.html")


@app.route("/ggk", methods=["POST", "GET"])
def ggk():
    if request.method == "POST":
        return render_template("ggk.html")
    else:
        return render_template("error.html")

@app.route("/it", methods=["POST", "GET"])
def it():
    if request.method == "POST":
        return render_template("it.html")
    else:
        return render_template("error.html")


@app.route("/it/praxis/caesar", methods=["POST", "GET"])
def it_praxis_caesar():
    if request.method == "GET":
        return render_template("ceasarCiffere.html")
    else:
        return render_template("error.html")

@app.route("/calculate", methods=["POST"])
def calculate():

    if request.method == "POST":
        text = ""
        shift = ""



        id, text, shift = request.form["id"], request.form["text"], request.form["shift"]
        print(text)
        try:
            erg = control.control(id, text, shift)
        except:
            return render_template("error.html")
        print(erg)

    return render_template("result.html", erg=erg)


if __name__ == '__main__':
    app.run(port=1337, debug=True, host="0.0.0.0")
