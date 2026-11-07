from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def accueil():

    parcelles = [
        {"nom": "Parcelle 1", "humidite": 35, "irrigation": "Arrêtée"},
        {"nom": "Parcelle 2", "humidite": 65, "irrigation": "Arrêtée"},
        {"nom": "Parcelle 3", "humidite": 25, "irrigation": "Arrêtée"},
        {"nom": "Parcelle 4", "humidite": 80, "irrigation": "Arrêtée"}
    ]

    for parcelle in parcelles:
        if parcelle["humidite"] < 30:
            parcelle["irrigation"] = "À activer"
        else:
            parcelle["irrigation"] = "Arrêtée"

    return render_template("index.html", parcelles=parcelles)


@app.route("/surveillance")
def surveillance():
    return render_template("surveillance.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)