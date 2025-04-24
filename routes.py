from main import app
from flask import render_template
from funcoes import *

@app.route("/")
def inicial():
    caixaTexto = paginaInicial()
    return render_template("index.html", caixaTexto=caixaTexto)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/servicos")
def servicos():
    paginas = servicosPagina()
    return render_template("servicos.html", paginas=paginas)

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/fakebook")
def fakebook():
    
    return render_template("fakebook.html")