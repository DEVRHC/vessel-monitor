from flask import Flask, render_template, request, redirect, url_for
from monitor import verificar_atividade, iniciar_monitoramento, parar_monitoramento, status_atual

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        navio = request.form["navio"]
        iniciar_monitoramento(navio)
        return redirect(url_for("index"))
    
    return render_template("index.html", status=status_atual())

@app.route("/parar")
def parar():
    parar_monitoramento()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
