from modulos_menu import * # importei o modulo menu do repositorio com * para não precisar digitar menu. antes de cada função
import pandas as pd # Para manipulação de dados do arquivo CSV nas funções do sistema


distancias = pd.read_csv('DNIT-distancias.csv', sep=';') # Lê o arquivo csv

while True:
    menu_principal = menu(['Consultar um Transporte', 'Cadastrar um Transporte', 
                           'Registro de Cadastros', 'Encerrar Sessão'], 'MENU PRINCIPAL')
    if menu_principal == 1:
        cabeçalho('Opção 1')
    elif menu_principal == 2:
        cabeçalho('Opção 2')
    elif menu_principal == 3:
        cabeçalho('Opção 3')
    elif menu_principal == 4:
        confirm = input('Tem certeza que deseja sair? (S/N) ').lower()
        while confirm != 's' or 'n':
            separador()
            confirm = input('Não entendi, por favor digite (S/N): ').lower()
            if confirm == 's':
                break
            elif confirm == 'n':
                break
        if confirm == 's':
                cabeçalho('Que pena! Até logo, volte sempre!')
                break
        elif confirm == 'n':
                continue
    else:
        print('Digite uma opção existente.')

