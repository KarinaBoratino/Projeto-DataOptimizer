from crypt import methods

from flask import Flask, render_template, request,redirect
from conexao.conexao import  conexao

app = Flask(__name__)

@app.route('/') #rota primaria
def hello_world():
    return render_template('inicial.html') #ele redireciona para a pagina inicial
@app.route('/login')
def inicial():
    return render_template('TLogin.html')

@app.route('/TCad')
def TCad():
    return render_template('TCad.html')

@app.route('/teste', methods=['GET'])
def test_conn():
    result = conexao()  # Testa a conexão
    return render_template('teste.html', result=result)

    return  conexao
if __name__ == '__main__':
    app.run()

#@app.route('logar', methods=['post'])
#def logar():
