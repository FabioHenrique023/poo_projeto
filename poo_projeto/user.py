class Usuario:
    def _init_(self, nome, login, senha, tipo, email, telefone):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.tipo = tipo
        self.email = email
        self.telefone = telefone

    def cadastrar_usario(self, info):
        user = "Fabio"
        if user == self.nome:
             return print(f'Usuário {self.nome} já cadastrado')
        return print(f'Usuário {self.nome} cadastrado com sucesso')
    
    # def listar_usuario(self, info):
    #     existe = "Fabio"
    #     if existe == self.nome:
    #         return print(f'Usuário existe: {self.nome}, {self.email}')
    #     return print("Usuário não existe")
    
    # def alterar_usuario(self, info):
    #     altera = "Tiago"
    #     if altera != self.nome:
            #return