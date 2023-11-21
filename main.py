from flask import Flask 
import random 

app = Flask(__name__)

@app.route("/")
def ciao_mondo():
    return '<h1>Ciao, Mondo!</h1><i><a href="/blog">cliccami!</i><br><i><a href="/crows">pagina speciale</i>'


@app.route("/crows")
def crows():
    return '<img src="https://picsum.photos/700/800" alt=""><br><i><a href="/">pagina iniziale</i>'

@app.route("/blog")
def fatti_casuali():
    fatti_random = ["La maggior parte delle persone che soffrono di dipendenza tecnologica sperimentano un forte stress quando si trovano al di fuori dell'area di copertura della rete o non possono utilizzare i loro dispositivi", "Secondo uno studio condotto nel 2018, più del 50% delle persone di età compresa tra i 18 e i 34 anni si considera dipendente dal proprio smartphone"]
    return f'<p>{random.choice(fatti_random)}</p><br><p>compiti per casa sono creare un altra pagina che faccia qualcosa tipo generare immagini casuali ecc e poi inviare il codice su github</p><br><i><a href = "/">ritorna_alla_pagina_iniziale</i>'

app.run(debug=True)

