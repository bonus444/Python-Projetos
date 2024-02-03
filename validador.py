import cliente
import empresa
import re
import os

def limparTela():
    os.system('cls')

def Senha():
    while True:
     sen = input('Digite sua senha: ')
     limparTela()
     if len(sen) < 8 or len(sen) > 15:
        print("A senha deve ter entre 8 e 15 caracteres")
     elif not re.search("[a-z]", sen):
        print("A senha deve conter pelo menos uma letra minúscula")
     elif not re.search("[A-Z]", sen):
        print("A senha deve conter pelo menos uma letra maiúscula")
     elif not re.search("[0-9]", sen):
        print("A senha deve conter pelo menos um número")
     elif not re.search("[@$!%*?&]", sen):
        print("A senha deve conter pelo menos um caractere especial (@$!%*?&)")
     else:
        return sen
     
      


while True:
    senha = Senha()
    print(senha)
    break