from modulos_menu import * # importei o modulo menu do repositorio com * para não precisar digitar menu. antes de cada função
import pandas as pd # Para manipulação de dados do arquivo CSV nas funções do sistema


distancias = pd.read_csv('DNIT-distancias.csv', sep=';') # Lê o arquivo csv

registro = 'tabela_registro.txt'
if not verificar_registro(registro):
     criar_registro(registro)


                    

while True:
    menu_principal = menu(['Consultar um Transporte', 'Cadastrar um Transporte', 
                           'Registro de Cadastros', 'Encerrar Sessão'], 'MENU PRINCIPAL')
    match menu_principal:
        case 1:
            cabeçalho('Opção 1')
        case 2:
            cabeçalho('Opção 2')
        case 3:
            cabeçalho('Opção 3')
        case 4:
            confirm = input('Tem certeza que deseja sair? (S/N) ').lower()
            match confirm:
                case 's':
                 cabeçalho('Que pena! Até logo, volte sempre!')
                case 'n':
                 continue
                case outro:
                 while confirm == 's' or 'n':
                    confirm = input('Não entendi, por favor digite (S/N): ')
                    match confirm:
                            case 's':
                                cabeçalho('Que pena! Até logo, volte sempre!')
                            case 'n':
                                break
        case outro:
                 print('Digite uma opção existente.')

       
