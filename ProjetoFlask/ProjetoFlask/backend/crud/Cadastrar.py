from Conexao.conexao import conectarSQLServer



def cadastrar_usuario(nome, email, ddd, telefone, senha, termos_aceitos):
    conexao = conectarSQLServer()
    if conexao is None:
        return "Erro ao conectar ao banco de dados."

    cursor = None
    try:
        cursor = conexao.cursor()


        cursor.execute('''
            INSERT INTO USUARIO_CLIENTE (nome, email, ddd, telefone, senha, aceitar_termos) 
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nome, email, ddd, telefone, senha, termos_aceitos))

        conexao.commit()
        return "Usuário cadastrado com sucesso."
    except Exception as e:

        mensagem_erro = str(e)


        if 'Viola\u00e7\u00e3o da restri\u00e7\u00e3o UNIQUE KEY' in mensagem_erro:
            return "O e-mail informado já está em uso. Por favor, utilize um e-mail diferente."
        else:
            return "Ocorreu um erro ao cadastrar o usuário. Por favor, tente novamente mais tarde."
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

