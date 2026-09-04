function convertUSD() {
    let usd = document.getElementById("usd").value;
    let arn = usd * 10;

    document.getElementById("resultUSD").innerHTML = "Результат: " + arn + " ARN";
}

function convertUAH() {
    let uah = document.getElementById("uah").value;
    let arn = uah * 0.23;

    document.getElementById("resultUAH").innerHTML = "Результат: " + arn.toFixed(2) + " ARN";
}

function convertEUR() {
    let eur = document.getElementById("eur").value;
    let arn = eur * 11.7;

    document.getElementById("resultEUR").innerHTML = "Результат: " + arn.toFixed(2) + " ARN"
}

function convertWFT() {
    let wft = document.getElementById("wft").value;
    let arn = wft * 5.714;

    document.getElementById("resultWFT").innerHTML = "Результат: " + arn.toFixed(2) + " ARN"
}