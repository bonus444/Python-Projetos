import mysql.connector

try:
    con = mysql.connector.connect(host='localhost',database ='Projeto',user='root',password='')

    criar_tabela_cliente = '''CREATE TABLE cliente(
                   id int not null auto_increment,
                   nome varchar(30) not null,
                   email varchar(30) not null,
                   cpf varchar(11) not null, 
                   login varchar(30) not null,
                   senha varchar(30) not null,
                   primary key(id)
                   )'''

    criar_tabela_empresa = '''CREATE TABLE empresa(
                   id int not null auto_increment,
                   nome varchar(30) not null,
                   email varchar(30) not null,
                   cnpj varchar(14)  not null,
                   login varchar(30) not null,
                   senha varchar(30) not null,
                   primary key(id)
                   )'''

    cursor = con.cursor()
    cursor.execute(criar_tabela_cliente)
    cursor.execute(criar_tabela_empresa)
    print('Tabelas criadas com sucesso!!')
except mysql.connector.Error as erro:
    print(f'Falha ao criar tabela: {erro}')

