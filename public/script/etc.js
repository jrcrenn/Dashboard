function Change() {
    if (document.getElementById("checkWeather").checked == true)
        document.getElementById("weather").style.display = "block";
    else
        document.getElementById("weather").style.display = "none";
    if (document.getElementById("checkTDL").checked == true)
        document.getElementById("ToDoList").style.display = "block";
    else
        document.getElementById("ToDoList").style.display = "none";
    if (document.getElementById("checkML").checked == true)
        document.getElementById("Lmovies").style.display = "block";
    else
        document.getElementById("Lmovies").style.display = "none";
    if (document.getElementById("checkMD").checked == true)
        document.getElementById("Dmovies").style.display = "block";
    else
        document.getElementById("Dmovies").style.display = "none";
    if (document.getElementById("checkMR").checked == true)
        document.getElementById("Amovies").style.display = "block";
    else
        document.getElementById("Amovies").style.display = "none";
    if (document.getElementById("checkCC").checked == true)
        document.getElementById("MoneyConverter").style.display = "block";
    else
        document.getElementById("MoneyConverter").style.display = "none";
}