class usuario:
    def __init__(self, email, nome, login, senha):
        self.id = None
        self.nome = nome
        self.login = login
        self.senha = senha
        self.email = email
        
    def get_id(self):
        return self.id 
    
    def set_id(self, id):
        self.id = id

    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome

    def get_login(self):
        return self.login
    
    def set_login(self, login):
        self.login = login

    def get_senha(self):
        return self.senha
    
    def set_senha(self, senha):
        self.senha = senha
    