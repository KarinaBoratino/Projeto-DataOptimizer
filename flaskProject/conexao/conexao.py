import pyodbc

def conectar_sql_server():
    # Configurações da conexão
    servidor = 'LAPTOP-T3V140D5'  # Nome do servidor conforme a imagem
    banco_dados = 'Data_Optimizer'  # Substitua pelo nome do seu banco de dados
    # Conectando ao SQL Server
    try:
        conexao = pyodbc.connect(
            f'DRIVER={{SQL Server}};SERVER={servidor};DATABASE={banco_dados};Trusted_Connection=yes;'
        )
        print("Conexão bem-sucedida ao SQL Server")
        return conexao
    except pyodbc.Error as e:
        print("Erro ao conectar ao SQL Server:", e)
        return None

# Uso da função
def conexao():
    conexao = conectar_sql_server()
    conexao.close()
    return  "conectado com sucesso"