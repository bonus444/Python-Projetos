from usuario import usuario

class cliente(usuario):
    def __init__(self, nome, cpf, email, login, senha):
        super.__init__(email, nome, login, senha)
        self.id = None
        self.cpf = cpf


    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id

    def get_cpf(self):
        return self.cpf
    
    def set_cpf(self, cpf):
        self.cpf = cpf
 
    