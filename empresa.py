from usuario import usuario

class empresa(usuario):
    def __init__(self, nome, cnpj, email, login, senha):
        super.__init__(email, nome, login, senha)
        self.id = None
        self.cnpj = cnpj


    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id

    def get_cnpj(self):
        return self.cnpj
    
    def set_cnpj(self, cnpj):
        self.cnpj = cnpj