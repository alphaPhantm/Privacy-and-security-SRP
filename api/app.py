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
def ggk_die_bevoelkerung_sollte_datenschutz_einen_h??heren_stellenwert_im_Leben_bekommen():
    return render_template("sollte_datenschutz_einen_h??heren_stellenwert_im_Leben_bekommen.html")

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

@app.route("/it/sicherheit/cia", methods=["POST", "GET"])
def it_sicherheit_cia():
    return render_template("cia.html")

@app.route("/it/sicherheit/verschluesselung", methods=["POST", "GET"])
def it_sicherheit_verschluesselung():
    return render_template("verschluesselung.html")

@app.route("/it/sicherheit/sicherheitskonzepte", methods=["POST", "GET"])
def it_sicherheit_sicherheitskonzepte():
    return render_template("sicherheitskonzepte.html")

@app.route("/it/hacking_cracking", methods=["POST", "GET"])
def it_hacking_cracking():
    return render_template("hackingCracking.html")

@app.route("/it/hacking_cracking/definitionen", methods=["POST", "GET"])
def it_hacking_cracking_definitionen():
    return render_template("definitionen.html")

@app.route("/it/hacking_cracking/hacking_techniken", methods=["POST", "GET"])
def it_hacking_cracking_hacking_techniken():
    return render_template("hackingTechniken.html")

@app.route("/it/hacking_cracking/brute_force", methods=["POST", "GET"])
def it_hacking_cracking_brute_force():
    return render_template("bruteForce.html")

@app.route("/it/hacking_cracking/haeufigkeitsanalyse", methods=["POST", "GET"])
def it_hacking_cracking_haeufigkeitsanalyse():
    return render_template("haeufigkeitsanalyse.html")

@app.route("/it/hacking_cracking/schwachstelle_mensch", methods=["POST", "GET"])
def it_hacking_cracking_schwachstelle_mensch():
    return render_template("schwachstelleMensch.html")

@app.route("/it/enigma", methods=["POST", "GET"])
def it_enigma():
    return render_template("enigma.html")

@app.route("/it/data_mining", methods=["POST", "GET"])
def it_data_mining():
    return render_template("itDataMining.html")

@app.route("/it/data_mining/was_ist_data_mining", methods=["POST", "GET"])
def it_data_mining_was_ist_data_mining():
    return render_template("wasIstDataMining.html")

@app.route("/it/data_mining/anwendungszwecke", methods=["POST", "GET"])
def it_data_mining_anwendungszwecke():
    return render_template("anwendungszwecke.html")

@app.route("/it/kuenstliche_inteligenz", methods=["POST", "GET"])
def it_kuenstliche_inteligenz():
    return render_template("kuenstliche_inteligenz.html")

@app.route("/it/kuenstliche_inteligenz/was_ist_eine_kuenstliche_intelligenz", methods=["POST", "GET"])
def it_kuenstliche_inteligenz_was_ist_eine_kuenstliche_intelligenz():
    return render_template("wasIstEineKuenstlicheIntelligenz.html")

@app.route("/it/kuenstliche_inteligenz/begriffserklaerung", methods=["POST", "GET"])
def it_kuenstliche_inteligenz_begriffserklaerung():
    return render_template("begriffserklaerung.html")

@app.route("/it/kuenstliche_inteligenz/schwache_und_starke_ki", methods=["POST", "GET"])
def it_kuenstliche_inteligenz_schwache_und_starke_ki():
    return render_template("schwacheUndStarkeKi.html")

@app.route("/it/kuenstliche_inteligenz/vor_und_nachteile", methods=["POST", "GET"])
def it_kuenstliche_inteligenz_vor_und_nachteile():
    return render_template("vorUndNachteile.html")

@app.route("/it/quantentechnologie", methods=["POST", "GET"])
def it_quantentechnologie():
    return render_template("quantentechnologie.html")

@app.route("/it/quantentechnologie/superposition", methods=["POST", "GET"])
def it_quantentechnologie_superposition():
    return render_template("superposition.html")

@app.route("/it/quantentechnologie/quantencomputer", methods=["POST", "GET"])
def it_quantentechnologie_quantencomputer():
    return render_template("quantencomputer.html")

@app.route("/it/quantentechnologie/der_tod_von_datenschutz", methods=["POST", "GET"])
def it_quantentechnologie_der_tod_von_datenschutz():
    return render_template("derTodVonDatenschutz.html")

@app.route("/it/quantentechnologie/quanten_internet", methods=["POST", "GET"])
def it_quantentechnologie_quanten_internet():
    return render_template("quantenInternet.html")

@app.route("/it/praxis", methods=["POST", "GET"])
def it_praxis():
    return render_template("itPraxis.html")



@app.route("/it/praxis/caesar_cipher", methods=["POST", "GET"])
def it_praxis_caesar_cipher():
    return render_template("ceasarCiffere.html")

@app.route("/it/praxis/caesar_cipher/algorithmus", methods=["POST", "GET"])
def it_praxis_caesar_cipher_algorithmus():
    return render_template("ceasarCiffereAlgo.html")

@app.route("/it/praxis/caesar_cipher_brute_force", methods=["POST", "GET"])
def it_praxis_caesar_cipher_brute_force():
    return render_template("ceasarCiffereBruteForce.html")

@app.route("/it/praxis/caesar_cipher_brute_force/algorithmus", methods=["POST", "GET"])
def it_praxis_caesar_cipher_brute_force_algorithmus():
    return render_template("ceasarCiffereBruteForceAlgo.html")

@app.route("/it/praxis/caesar_cipher_analyse", methods=["POST", "GET"])
def it_praxis_caesar_cipher_analyse():
    return render_template("ceasarCiffereAnalyse.html")

@app.route("/it/praxis/caesar_cipher_analyse/algorithmus", methods=["POST", "GET"])
def it_praxis_caesar_cipher_analyse_algorithmus():
    return render_template("ceasarCiffereAnalyseAlgo.html")

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

@app.route("/it/praxis/enigma_brute_force", methods=["POST", "GET"])
def it_praxis_enigma_brute_force():
    return render_template("enigmaBruteForce.html")

@app.route("/it/praxis/enigma_brute_force/algorithmus", methods=["POST", "GET"])
def it_praxis_enigma_brute_force_algorithmus():
    return render_template("enigmaBruteForceAlgo.html")

@app.route("/it/praxis/rsa", methods=["POST", "GET"])
def it_praxis_enigma_rsa():
    return render_template("rsa.html")

@app.route("/it/praxis/rsa/algorithmus", methods=["POST", "GET"])
def it_praxis_enigma_rsa_algorithmus():
    return render_template("rsaAlgorithmus.html")



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

@app.route("/it/praxis/calculate/rsa", methods=["POST"])
def calculate_rsa():
    if request.method == "POST":

        bits = request.form["bits"]
        bits = int(bits)
        text = request.form["text"]
        public_key = request.form["publicKey"]

        privateKey, publicKey, geheim_text = control.control_rsa(bits, text, public_key)

    return render_template("result_rsa.html", privateKey=privateKey, publicKey=publicKey, geheim_text=geheim_text)


@app.errorhandler(404)
def error(e):
    return render_template("error.html")

if __name__ == '__main__':
    app.run(port=1337, debug=True, host="0.0.0.0")
