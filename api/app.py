from flask import Flask, render_template, request
import control

app = Flask(__name__, template_folder="../templates", static_folder="../static")


@app.route("/")
def index():
    return render_template("ceasarCiffere.html")

@app.route("/calculate", methods=["POST"])
def calculate():

    if request.method == "POST":
        text = ""
        shift = ""



        id, text, shift = request.form["id"], request.form["text"], request.form["shift"]
        print(text)
        erg = control.control(id, text, shift)
        print(erg)

    return render_template("result.html", erg=erg)


if __name__ == '__main__':
    app.run(port=1337, debug=True)
