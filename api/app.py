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

@app.route("/ggk/geschichte/altertum", methods=["POST", "GET"])
def ggk_geschichte_altertum():
    return render_template("altertum.html")

@app.route("/ggk/geschichte/mittelalter", methods=["POST", "GET"])
def ggk_geschichte_mittelalter():
    return render_template("mittelalter.html")

@app.route("/ggk/geschichte/renaissance", methods=["POST", "GET"])
def ggk_geschichte_renaissance():
    return render_template("renaissance.html")

@app.route("/ggk/geschichte/19_jahrhundert", methods=["POST", "GET"])
def ggk_geschichte_19_jahrhundert():
    return render_template("19Jahrhundert.html")

@app.route("/ggk/geschichte/1_weltkrieg", methods=["POST", "GET"])
def ggk_geschichte_1_weltkrieg():
    return render_template("1Weltkrieg.html")

@app.route("/ggk/geschichte/2_weltkrieg", methods=["POST", "GET"])
def ggk_geschichte_2_weltkrieg():
    return render_template("2Weltkrieg.html")

@app.route("/ggk/ueberwachungsstaaten", methods=["POST", "GET"])
def ggk_ueberwachungsstaaten():
    return render_template("ueberwachungsstaaten.html")

@app.route("/ggk/ueberwachungsstaaten/was_macht_einen_ueberwachungsstaat_aus", methods=["POST", "GET"])
def ggk_ueberwachungsstaaten_was_macht_einen_ueberwachungsstaat_aus():
    return render_template("wasMachtEinenUeberwachungsstaatAus.html")

@app.route("/ggk/ueberwachungsstaaten/ist_china_ein_ueberwachungsstaat", methods=["POST", "GET"])
def ggk_ueberwachungsstaaten_ist_china_ein_ueberwachungsstaat():
    return render_template("istChinaEinUeberwachungsstaat.html")

@app.route("/ggk/ueberwachungsstaaten/ist_deutschland_ein_ueberwachungsstaat", methods=["POST", "GET"])
def ggk_ueberwachungsstaaten_ist_deutschland_ein_ueberwachungsstaat():
    return render_template("istDeutschlandEinUeberwachungsstaat.html")

@app.route("/ggk/ueberwachungsstaaten/politische_rahmenbedingungen", methods=["POST", "GET"])
def ggk_ueberwachungsstaaten_politische_rahmenbedingungen():
    return render_template("politische_rahmenbedingungen.html")

@app.route("/ggk/ueberwachungsstaaten/edward_snowden", methods=["POST", "GET"])
def ggk_ueberwachungsstaaten_edward_snowden():
    return render_template("edward_snowden.html")

@app.route("/ggk/ueberwachungsstaaten/resuemee", methods=["POST", "GET"])
def ggk_ueberwachungsstaaten_resuemee():
    return render_template("resuemee.html")

@app.route("/ggk/data_mining", methods=["POST", "GET"])
def ggk_data_mining():
    return render_template("dataMining.html")

@app.route("/ggk/data_mining/einfuehrung", methods=["POST", "GET"])
def ggk_data_mining_einfuehrung():
    return render_template("einfuehrung.html")

@app.route("/ggk/data_mining/biometrische_gesichtserkennung", methods=["POST", "GET"])
def ggk_data_mining_biometrische_gesichtserkennung():
    return render_template("biometrische_gesichtserkennung.html")

@app.route("/ggk/data_mining/geotracking_triangulation", methods=["POST", "GET"])
def ggk_data_mining_geotracking_triangulation():
    return render_template("geotracking_triangulation.html")

@app.route("/ggk/data_mining/wer_sammelt_unsere_daten", methods=["POST", "GET"])
def ggk_data_mining_wer_sammelt_unsere_daten():
    return render_template("wer_sammelt_unsere_daten.html")

@app.route("/ggk/data_mining/was_passiert_mit_unseren_daten", methods=["POST", "GET"])
def ggk_data_mining_was_passiert_mit_unseren_daten():
    return render_template("was_passiert_mit_unseren_daten.html")

@app.route("/ggk/die_bevoelkerung", methods=["POST", "GET"])
def ggk_die_bevoelkerung():
    return render_template("die_bevoelkerung.html")

@app.route("/ggk/die_bevoelkerung/ist_der_datenschutz_vielen_noch_wichtig", methods=["POST", "GET"])
def ggk_die_bevoelkerung_ist_der_datenschutz_vielen_noch_wichtig():
    return render_template("ist_der_datenschutz_vielen_noch_wichtig.html")

@app.route("/ggk/die_bevoelkerung/sollte_datenschutz_einen_hoeheren_stellenwert_im_Leben_bekommen", methods=["POST", "GET"])
def ggk_die_bevoelkerung_sollte_datenschutz_einen_höheren_stellenwert_im_Leben_bekommen():
    return render_template("sollte_datenschutz_einen_höheren_stellenwert_im_Leben_bekommen.html")

@app.route("/ggk/die_bevoelkerung/kann_man_sich_ueberhaupt_schuetzen", methods=["POST", "GET"])
def ggk_die_bevoelkerung_kann_man_sich_ueberhaupt_schuetzen():
    return render_template("kann_man_sich_ueberhaupt_schuetzen.html")

@app.route("/ggk/zukunft", methods=["POST", "GET"])
def ggk_zukunft():
    return render_template("zukunft.html")

@app.route("/ggk/zukunft/fortschritt", methods=["POST", "GET"])
def ggk_zukunft_fortschritt():
    return render_template("fortschritt.html")

@app.route("/ggk/zukunft/sind_kulturelle_werte_mit_den_neuen_technologien_vereinbar", methods=["POST", "GET"])
def ggk_zukunft_sind_kulturelle_werte_mit_den_neuen_technologien_vereinbar():
    return render_template("sind_kulturelle_werte_mit_den_neuen_technologien_vereinbar.html")

@app.route("/ggk/zukunft/wie_wird_datenschutz_und_sicherheit_in_zukunft_aussehen", methods=["POST", "GET"])
def ggk_zukunft_wie_wird_datenschutz_und_sicherheit_in_zukunft_aussehen():
    return render_template("wie_wird_datenschutz_und_sicherheit_in_zukunft_aussehen.html")

@app.route("/it", methods=["POST", "GET"])
def it():
    return render_template("it.html")

@app.route("/it/sicherheit", methods=["POST", "GET"])
def it_sicherheit():
    return render_template("sicherheit.html")

@app.route("/it/hacking_cracking", methods=["POST", "GET"])
def it_hacking_cracking():
    return render_template("hackingCracking.html")

@app.route("/it/enigma", methods=["POST", "GET"])
def it_enigma():
    return render_template("enigma.html")

@app.route("/it/data_mining", methods=["POST", "GET"])
def it_data_mining():
    return render_template("itDataMining.html")

@app.route("/it/kuenstliche_inteligenz", methods=["POST", "GET"])
def it_kuenstliche_inteligenz():
    return render_template("kuenstliche_inteligenz.html")

@app.route("/it/quantentechnologie", methods=["POST", "GET"])
def it_quantentechnologie():
    return render_template("quantentechnologie.html")

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


@app.errorhandler(404)
def error(e):
    return render_template("error.html")

if __name__ == '__main__':
    app.run(port=1337, debug=True, host="0.0.0.0")
