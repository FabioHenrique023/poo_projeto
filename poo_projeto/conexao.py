import psycopg2

def conectar():
    try:
        conexao = psycopg2.connect(
            host = "localhost",
            database = "biblioteca",
            user = "postgres",
            password = "123456"
        )
        cursor = conexao.cursor()
        return conexao, cursor
    except Exception as erro:
        print(f"Erro ao conectar ao banco {erro}")
        return None, None

def desconectar(cursor, conexao):
    if conexao:
        conexao.close()
    if cursor:
        cursor.close()
        
#TESTANDO A CONEXÃO

# conexao, cursor = conectar()

# if conexao:
#     cursor.execute("SELECT * FROM tipo_usuario")
#     registros = cursor.fetchall()
#     for i in registros:
#         print(i)

#     desconectar(conexao, cursor)        
