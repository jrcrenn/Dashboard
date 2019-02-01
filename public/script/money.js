function calc() {
    var valSrc = document.getElementById("curSrc").value;
    var valDst = document.getElementById("curDst").value;
    var valQte = document.getElementById("qte").value;
    $.ajax({
        url: 'https://api.exchangeratesapi.io/latest?base=' + valSrc,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            var currency = data.rates;
            Object.entries(currency).forEach(
                ([cle, valeur]) => {
                    for (i in cle) {
                        if (valDst == `${cle}`) {
                            var res = (`${valeur}` * valQte);
                            document.getElementById("result").innerHTML = res.toFixed(2);
                        }
                    }
                });
            if (valDst == valSrc)
                document.getElementById("result").innerHTML = valQte;
        }
    })
}