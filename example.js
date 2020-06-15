// Nur fürs ausgeben
function reqListener () {
    console.log(this.responseText);
}

//Auslesen aller events
var oReq = new XMLHttpRequest();
    oReq.addEventListener("load", reqListener);
    oReq.open("GET", "https://76brg3dsq1.execute-api.eu-central-1.amazonaws.com/prod/events");
    oReq.send();



//Eintragen
var oReq = new XMLHttpRequest();
    oReq.open("POST", "https://76brg3dsq1.execute-api.eu-central-1.amazonaws.com/prod/events");
    oReq.addEventListener("load", reqListener);
    oReq.send(JSON.stringify({
        "event": "newEvent5",
            "information": {
                    "year": "2020",
                    "title": "first event"
             }
        }
    ));
