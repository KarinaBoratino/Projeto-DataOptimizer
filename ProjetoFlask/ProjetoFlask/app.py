# app.py

from flask import Flask, render_template, request, jsonify
from backend.crud.Cadastrar import cadastrar_usuario  # Importando a nova função
from Conexao.conexao import conectarBanco, conectarSQLServer
from backend.crud.verificar_usuario import verificar_usuario

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        ddd = request.form['ddd']
        telefone = request.form['telefone']
        senha = request.form['senha']

        termos_aceitos = 1 if request.form.get('termos') == 'on' else 2

        resultado = cadastrar_usuario(nome, email, ddd, telefone, senha, termos_aceitos)

        if "sucesso" in resultado:
            return jsonify({'success': True}), 200
        else:
            return jsonify({'success': False, 'message': resultado}), 400
    else:
        return render_template("Cadastrar.html")

@app.route('/login', methods=['POST'])  # Nova rota para login
def login():
    email = request.form['email']
    senha = request.form['senha']

    if verificar_usuario(email, senha):
        return jsonify({'success': True, 'message': 'Login realizado com sucesso!'}), 200
    else:
        return jsonify({'success': False, 'message': 'Credenciais inválidas. Tente novamente.'}), 401

@app.route('/conexao')
def conexaoserver():
    resultado = conectarSQLServer()
    return render_template('testeconexao/conexaoServer.html', resultado=resultado)

@app.route('/conexaomysql')
def conexaomysql():
    resultado = conectarBanco()
    return render_template('testeconexao/conexaomysql.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
