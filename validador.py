import cliente
import empresa
import re
import os
import banco


def limparTela():
    os.system('cls')

def nome():
   while True:
      nom = input('Digite seu nome: ')
      if nom == '':
         print('Digite um nome valido.')
         input('Digite enter para continuar...')
         limparTela()
         continue
      temp = nom.replace(' ', '')
      if any(i.isdigit() for i in temp):
         print('O nome não deve conter números.')
         limparTela()
         continue
      else:
         return temp

def cpf():
      while True:
            Cp = input('Digite seu cpf: ')
            if Cp == '':
                print('Digite um cpf valido..')
                input('pressione enter para continuar...')
                limparTela()
                continue 
            if len(Cp) < 11 or len(Cp) > 11:
               print('O cpf deve conter 11 digitos')
               input('pressione enter para continuar...')
               limparTela()
               continue 
            else:
               return Cp

def cnpj():
        while True:
            c = input('Digite seu cnpj: ')
            if c == '':
                print('Digite um cnpj valido..')
                input('pressione enter para continuar...')
                limparTela()
                continue 
            if len(c) < 14 or len(c) > 14:
               print('O cnpj deve conter 14 digitos')
               input('pressione enter para continuar...')
               limparTela()
               continue 
            te = c.replace(' ', '')
            if any(i.isnumeric() for i in te):
               print('So pode conter numeros..')
               input('pressione enter para continuar...')
               limparTela()
               continue 
            else:
               return te
def email():
   while True:
    em = input('Digite seu email: ')
    if em == '':
        print('Digite um email valido...')
        input('pressione enter para continuar...')
        limparTela()
        continue
    else: 
        return em
        
      
def login():
   while True:
      lo = input('Digite seu login: ')
      if lo == '':
         print('Digite um login valido.')
         input('pressione enter para continuar...')
         limparTela()
         continue
      temp = lo.replace(' ', '')
      if temp:
         return temp

def senha():
    while True:
     sen = input('Digite sua senha: ')
     limparTela()
     if len(sen) < 8 or len(sen) > 15:
        print("A senha deve ter entre 8 e 15 caracteres")
        input('pressione enter para continuar...')
        limparTela()
     elif not re.search("[a-z]", sen):
        print("A senha deve conter pelo menos uma letra minúscula")
        input('pressione enter para continuar...')
        limparTela()
     elif not re.search("[A-Z]", sen):
        print("A senha deve conter pelo menos uma letra maiúscula")
        input('pressione enter para continuar...')
        limparTela()
     elif not re.search("[0-9]", sen):
        print("A senha deve conter pelo menos um número")
        input('pressione enter para continuar...')
        limparTela()
     else:
        return sen
     
def inserir_cliente(nome, email, cpf, login, senha):
   try:
        
        co = f'INSERT INTO cliente (nome, email, cpf, login, senha) VALUES ("{nome}","{email}","{cpf}","{login}","{senha}")'
        banco.cursor.execute(co)
        banco.con.commit()

        print("Usuário cadastrado com sucesso!")

   except ValueError as e:
        print(f"Erro: {e}")
