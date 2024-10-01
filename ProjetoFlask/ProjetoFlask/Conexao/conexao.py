from configDados import DADOS, SQLSERVER
import mysql.connector
import pyodbc

def conectarBanco():
    try:
        conexao = mysql.connector.connect(**DADOS)
        if conexao.is_connected():
            print("Conectado com sucesso ao banco de dados MySQL")
            return conexao  # Retorna o objeto de conexão
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None  # Retorna None em caso de erro

def conectarSQLServer():
    try:
        conexao = pyodbc.connect(
            f'DRIVER={{SQL Server}};SERVER={SQLSERVER["servidor"]};DATABASE={SQLSERVER["database"]};Trusted_Connection=yes;'
        )
        print("Conectado com sucesso ao banco de dados SQL Server")
        return conexao  # Retorna o objeto de conexão
    except pyodbc.Error as erro:
        print(f"Erro ao conectar ao SQL Server: {erro}")
        return None  # Retorna None em caso de erro
