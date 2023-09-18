from conexao import Conexao as bd
import psycopg2


class TipoUsuario:
    def __init__(self, nome):
        self.nome = nome
        
    def usuer_existe(self):
        try:
            conexao = bd().conectar()
            cursor = conexao.cursor()
            
            #CONSULTAR USUÁRIO
            sql = "SELECT id FROM tipo_usuario WHERE nome = %s;"
            
            cursor.execute(sql, (self.nome,))
            
            resultado = cursor.fetchone()
            
            #FECHAR A CONEXÃO
            cursor.close()
            conexao.close()
            
            return resultado is not None
        
        except psycopg2.Error as error:
            print(f"Não foi possível criar o usuário {error}")
                
    def create_tipousuario(self):
        if not self.usuer_existe:
            try:
                
    
    def update_tipousuario(self):
        pass
    
    def read_tipousuario(self):
        pass