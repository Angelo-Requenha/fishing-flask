from main import app
from flask import render_template, request, url_for, redirect, flash
import sqlite3
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

@app.route("/fakebookLogin", methods=["GET", "POST"])
def fakebook():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        con = sqlite3.connect('DB/db.sqlite')
        cur = con.cursor()
        cur.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
        user = cur.fetchone()
        con.close()
        
        if user:
            # Redireciona para a página inicial se o login for bem-sucedido
            return redirect(url_for('home', nome=user[3]))
            
    return render_template("fakebookLogin.html")

@app.route("/fakebookCreate", methods=["GET", "POST"])
def fakebookCreate():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        nome = request.form['nome']

        con = sqlite3.connect('DB/db.sqlite')
        cur = con.cursor() 
        cur.execute("INSERT INTO usuarios (email, senha, nome) VALUES (?, ?, ?)", (email, senha, nome))
        con.commit()
        con.close()
    
    return render_template("fakebookCreate.html")

@app.route("/home/<nome>")
def home(nome):
    return render_template("fakebookInicio.html", nome=nome)