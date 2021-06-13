function myFunction() {
    if (document.getElementById("id").getAttribute("value") === "1"){
        document.getElementById("id").setAttribute("value", "0")
        document.getElementById("submit").setAttribute("value", "Verschlüsseln")
    }
    else {
        document.getElementById("id").setAttribute("value", "1")
        document.getElementById("submit").setAttribute("value", "Entschlüsseln")
    }

}