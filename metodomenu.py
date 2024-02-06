import validador
import banco


id_usuario_autenticado = None
id_empresa_autenticada = None

def main():
    while True:
        validador.limparTela()
        print("============================================================")
        print("|                       MENU                              |")
        print("|                                                          |")
        print("============================================================")
        print("\nOpções:")
        print("1. Cadastrar")
        print("2. Entrar (Login)")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            validador.limparTela()
            print('Escolha o tipo de cadastro:')
            print('1. Cadastro de Usuário')
            opcao = input("Escolha uma opção:")
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