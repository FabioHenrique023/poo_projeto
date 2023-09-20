import psycopg2

class Conexao:
    def __init__(self):
        self.host = "localhost"
        self.database = "biblioteca"
        self.user = "postgres"
        self.password = "123456"
        self.conexao = None
        self.cursor = None
        
    def conectar(self):
        try:
            self.conexao = psycopg2.connect(
                host = self.host,
                database = self.database,
                user = self.user,
                password = self.password
            )
            self.cursor = self.conexao.cursor()
            return self.conexao
        
        except psycopg2.Error as erro:
            print(f"Erro ao se conectar: {erro}")
    
    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()