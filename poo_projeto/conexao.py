import psycopg2

class Conexao:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conexao = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexao = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.conexao.cursor()
        except Exception as erro:
            print(f"Erro ao conectar ao banco: {erro}")

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()

# Exemplo de uso
conexao_config = {
    "host": "localhost",
    "database": "biblioteca",
    "user": "postgres",
    "password": "123456"
}

conexao = Conexao(**conexao_config)
conexao.conectar()

if conexao.conexao:
    conexao.cursor.execute("SELECT * FROM tipo_usuario")
    registros = conexao.cursor.fetchall()
    for i in registros:
        print(i)

conexao.desconectar()
