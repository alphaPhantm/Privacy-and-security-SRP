from flask import Flask, render_template, request, url_for, redirect
import control

app = Flask(__name__)

app.template_folder = "../templates"
app.static_folder = "../static/"


@app.route("/")
def index():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("landingpage.html")

@app.route("/me")
def me():
    return render_template("me.html")

@app.route("/ggk", methods=["POST", "GET"])
def ggk():
    return render_template("ggk.html")

@app.route("/ggk/geschichte", methods=["POST", "GET"])
def ggk_geschichte():
    return render_template("geschichte.html")

@app.route("/ggk/ueberwachungsstaaten", methods=["POST", "GET"])
def ggk_ueberwachungsstaaten():
    return render_template("ueberwachungsstaaten.html")

@app.route("/ggk/data_mining", methods=["POST", "GET"])
def ggk_data_mining():
    return render_template("dataMining.html")

@app.route("/ggk/die_bevoelkerung", methods=["POST", "GET"])
def ggk_die_bevoelkerung():
    return render_template("die_bevoelkerung.html")

@app.route("/ggk/zukunft", methods=["POST", "GET"])
def ggk_zukunft():
    return render_template("zukunft.html")

@app.route("/it", methods=["POST", "GET"])
def it():
    return render_template("it.html")



@app.route("/it/praxis", methods=["POST", "GET"])
def it_praxis():
    return render_template("itPraxis.html")



@app.route("/it/praxis/caesar_cipher", methods=["POST", "GET"])
def it_praxis_caesar_cipher():
    return render_template("ceasarCiffere.html")


@app.route("/it/praxis/caesar_cipher/algorithmus", methods=["POST", "GET"])
def it_praxis_caesar_cipher_algorithmus():
    return render_template("ceasarCiffereAlgo.html")

@app.route("/it/praxis/vigenere_cipher", methods=["POST", "GET"])
def it_praxis_vigenere_cipher():
    return render_template("vigenere_cipher.html")


@app.route("/it/praxis/vigenere_cipher/algorithmus", methods=["POST", "GET"])
def it_praxis_vigenere_cipher_algorithmus():
    return render_template("vigenere_cipherAlgo.html")



@app.route("/it/praxis/skytale", methods=["POST", "GET"])
def it_praxis_skytale():
    return render_template("skytale.html")


@app.route("/it/praxis/skytale/algorithmus", methods=["POST", "GET"])
def it_praxis_skytale_algorithmus():
    return render_template("skytaleAlgo.html")


@app.route("/it/praxis/enigma", methods=["POST", "GET"])
def it_praxis_enigma():
    return render_template("enigma.html")

@app.route("/it/praxis/enigma/algorithmus", methods=["POST", "GET"])
def it_praxis_enigma_algorithmus():
    return render_template("enigmaAlgo.html")



@app.route("/it/praxis/calculate", methods=["POST"])
def calculate():
    if request.method == "POST":
        text = ""
        shift = ""
        passPhrase = ""


        id = request.form["id"]
        text = request.form["text"]
        shift = request.form["shift"]
        passPhrase = request.form["passPhrase"]
        ukw = request.form["ukw"]
        walze1 = request.form["walze1"]
        walze2 = request.form["walze2"]
        walze3 = request.form["walze3"]
        walzenPos = request.form["walzenPos"]
        ringPosW1 = request.form["ringPosW1"]
        ringPosW2 = request.form["ringPosW2"]
        ringPosW3 = request.form["ringPosW3"]
        steckerbrett = request.form["steckerbrett"]

        erg = control.control(id, text, shift, passPhrase, ukw, walze1, walze2, walze3, walzenPos, ringPosW1, ringPosW2, ringPosW3, steckerbrett)
        print(erg)

    return render_template("result.html", erg=erg)


if __name__ == '__main__':
    app.run(port=1337, debug=True, host="0.0.0.0")
