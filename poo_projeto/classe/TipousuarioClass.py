from classe.ConexaoClass import Conexao as bd
import psycopg2


class TipoUsuario:
    def __init__(self):
        self.id = None
        self.nome = None
            
    def user_existe(self):
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
    
    def solicitar_usuario(self):
        self.nome = input("Digite o tipo de usuário: ")
                
    def create_tipousuario(self):
        self.solicitar_usuario()
        if not self.user_existe():
            try:
                conexao = bd().conectar()
                cursor = conexao.cursor()
                
                sql_insert = "INSERT INTO tipo_usuario(nome) VALUES(%s) RETURNING id;"
                
                cursor.execute(sql_insert, (self.nome,))
                
                novo_id = cursor.fetchone()[0]

                conexao.commit()
                
                cursor.close()
                conexao.close()
                
                print(f"Usuário cadastrado com sucesso: {novo_id}")
                
                bd().desconectar()
            
            except psycopg2.Error as erro:
                print(f"Houve uma excessão: {erro}")
        else:
            print("Usuário já existe no banco de dados!")
    def update_tipousuario(self):
        pass
    
    def get_tiposusuario(self):
        try:
            conexao = bd().conectar()
            cursor = conexao.cursor()

            # CONSULTAR TIPOS DE USUÁRIO
            sql = "SELECT id, nome FROM tipo_usuario;"

            cursor.execute(sql)
            resultados = cursor.fetchall()

            # FECHAR A CONEXÃO
            cursor.close()
            conexao.close()

            tipos_usuario = [{"id": id, "nome": nome} for id, nome in resultados]

            return tipos_usuario

        except psycopg2.Error as error:
            print(f"Não foi possível recuperar os tipos de usuário: {error}")
