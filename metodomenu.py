import validador
import banco


id_usuario_autenticado = None
id_empresa_autenticada = None

def main():
    while True:
        validador.limparTela()
        print('============================================================')
        print('|                       Estoque                            |')
        print('|                       projeto                            |')
        print('============================================================\n')
        print('--------------------')
        print('| 1. Cadastrar     |')
        print('--------------------')
        print('| 2. Entrar (Login)|')
        print('--------------------')
        print('| 3. Sair          |')
        print('--------------------')
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            validador.limparTela()
            print('==============================')
            print('| Escolha o tipo de cadastro |')
            print('==============================\n')
            print('-------------------------')
            print('| 1. Cadastro de Cliente|')
            print('-------------------------')
            print('| 2. Cadastro Empresa   |')
            print('-------------------------')
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
             while True:
              try:
               nome = validador.nome()
               email = validador.email()
               cpf = validador.cpf()
               login = validador.login()
               senha = validador.senha()
               validador.inserir_cliente(nome, email, cpf, login, senha)
               print('Criado com sucesso!!!')
               break
              except ValueError as ve:
               print(f'{ve}')
               input('pressione enter para continuar...')
               validador.limparTela()
               continue
              except Exception as e:
               print(f'{e}')
            if opcao == '2':
             while True:
              try:
               nome = validador.nome()
               email = validador.email()
               cnpj = validador.cnpj()
               login = validador.login()
               senha = validador.senha()
               validador.inserir_empresa(nome, email, cnpj, login, senha)
               print('Criado com sucesso!!!')
               break
              except ValueError as ve:
               print(f'{ve}')
               input('pressione enter para continuar...')
               validador.limparTela()
               continue
              except Exception as e:
               print(f'{e}')
        if escolha == '2':
          print('===========================')
          print('|     Faça seu login      |')
          print('===========================\n')
          print('-----------------------')
          print('| 1. login de Cliente |')
          print('-----------------------')
          print('| 2. login Empresa    |')
          print('-----------------------')
          opcão = input('Digite: ')
          if opcão == '1':
           login = input('Login: ')
           senha = input('Senha: ')
           authenticado = validador.logCL(login, senha)
           if authenticado:
             while True:
              print('============================================================')
              print('|                       BEM VINDO                          |')
              print(f'|                   {authenticado[1]}                     |')
              print('============================================================\n')
              print('--------------------')
              print('| 1. estoque       |')
              print('--------------------')
              print('| 2. ..............|')
              print('--------------------')
              print('| 3. Sair          |')
              print('--------------------')
              escolha = input("Escolha uma opção: ")
             

           
