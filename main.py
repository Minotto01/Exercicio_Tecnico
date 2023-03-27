from modulos_menu import * # importei o modulo menu do repositorio com * para não precisar digitar menu. antes de cada função
import pandas as pd # Para manipulação de dados do arquivo CSV nas funções do sistema
from time import sleep

distancias = pd.read_csv('DNIT-distancias.csv', sep=';') # Lê o arquivo csv

registro = 'tabela_registro.txt'
if not verificar_registro(registro):
     criar_registro(registro)

while True: # loop menu
    menu_principal = menu(['Consultar um Transporte', 'Cadastrar um Transporte', 'Registro de Transportes', 'Encerrar Sessão'], 'MENU PRINCIPAL')
    match menu_principal:
        case 1:
            cabeçalho('CONSULTAR UM TRANSPORTE')
            # mostrar trechos disponiveis
            # escolher 2
            # escolher modalidade
            # distancia, custo total, se não existir,
            print('Digite o nome das cidades de partida e destino'.center(50))
            print('Cidades disponíveis: '.center(50))
            cabeçalho('MODALIDADES\nCaminhão de PEQUENO porte, Caminhão de MÉDIO porte e Caminhão de GRANDE porte')
            partida = input('Digite a cidade de partida: ')
            destino = input('Digite a cidade de destino: ')
            porte = input('Digite o porte do caminhão: ')
            lista_cidades = [] # usar o csv

            if partida or destino not in lista_cidades:
                print('Desculpe, essa cidade não está disponível ou não existe.')
            else:
               print(f'De {partida} para {destino}, utilizando um caminhão de {porte} porte, a distância é de xkm e o \n custo de R$x')
               break
        case 2:
            cabeçalho('CADASTRAR UM TRANSPORTE') 
        # receber 2 ou mais cidades e 1 ou mais itens, responder o trajeto total e caminhão mais adequado
        # custo por trecho e total
            sleep(1.5)

            trajeto = []

            n_cidades = int(input('Digite o número total de cidades do trajeto: '))
            origem = input('Digite o nome da cidade de origem: ')
            trajeto.append(origem)

            for i in range(1, n_cidades):
                cidades = str(input('Digite o nome da próxima cidade: '))
                trajeto.append(cidades)

            itens = []
            quantidades = []

            n_itens = verif_int('Quantos tipos diferentes de itens você gostaria de transportar: ')

            for i in range(0, n_itens):
                item = (input('Digite o nome do item: '))
                quant_item = (input('Digite sua quantidade: '))
                itens.append(item)
                quantidades.append(quant_item) 

            print(quantidades)              
            print(itens)
            print(trajeto)

            break
        case 3:
            cabeçalho('REGISTRO DE TRANSPORTES')
            ler_registro(registro)
            break
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
            break
        case outro:
                 print('Digite uma opção existente.')
    sleep(2)   

       
