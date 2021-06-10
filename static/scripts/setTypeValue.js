function myFunction() {
    if (document.getElementById("id").getAttribute("value") === 1){
        document.getElementById("id").setAttribute("value", 0)
    }
    else {
        document.getElementById("id").setAttribute("value", 1)
    }
}