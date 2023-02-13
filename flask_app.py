
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import datetime, requests

app = Flask(__name__)

messages = [{"contenu": "Admirable !",
    "auteur":"Moi-même",
    "heure": "Aujourd'hui à la même heure"},
    {"contenu": "ça pourrait être mieux",
    "auteur": "Bob",
    "heure": "dans trois ans"}
    ]

@app.route('/')
def index():
    return render_template('accueil.html', messages=messages)

@app.route("/envois/", methods=["POST"])
def envois():
    contenu = request.form["contenu"]
    destinataire = request.form["destinataire"]
    auteur = request.base_url.split(".")[0].split("/")[-1]

    if destinataire == auteur:
        return f"Pas le droit de s'auto-envoyer un message destinataire == {auteur}"

    url_destinataire = f"https://{destinataire}.pythonanywhere.com/reception/"
    heure = datetime.datetime.now().strftime("%H:%M:%S le %d %m %Y")
    payload = {"contenu": contenu, "auteur": auteur, "heure": heure}
    reponse_json = requests.post(url=url_destinataire, data=payload)
    return reponse_json.content.decode()

@app.route("/reception/", methods=["POST"])
def reception():
    contenu = request.form["contenu"]
    auteur = request.form["auteur"]
    heure = request.form["heure"]
    # ...
    time.sleep(0.1)

    return "Votre message a bien été réceptionné chez <b>mkone2</b> Al-Adin et vos mots sont déjà en train de prendre vie, dans l'univers des mille-et-une nuits.  Merci !"
