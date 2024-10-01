from Conexao.conexao import conectarSQLServer

def verificar_usuario(email, senha):
    try:
        conexao = conectarSQLServer()
        if conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM USUARIO_CLIENTE WHERE email = ? AND senha = ?", (email, senha))
            usuario = cursor.fetchone()
            cursor.close()
            conexao.close()
            return usuario is not None  # Retorna True se o usuário existir
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    return False  # Retorna False em caso de erro ou se o usuário não existir
