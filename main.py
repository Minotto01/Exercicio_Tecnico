from modulos_menu import * # importei o modulo menu do repositorio com * para não precisar digitar menu. antes de cada função
from time import sleep
import csv

with open('DNIT-distancias.csv', 'r') as tabela:
    ler = csv.reader(tabela, delimiter=';')
    lista_linhas = list(ler)

cidades = lista_linhas[0]

registro = 'tabela_registro.txt'
if not verificar_registro(registro):
     criar_registro(registro)

while True: # loop menu
    menu_principal = menu(['Consultar um Transporte', 'Cadastrar um Transporte', 'Registro de Transportes', 'Encerrar Sessão'], 'MENU PRINCIPAL')
    match menu_principal:
        case 1:
            cabeçalho('CONSULTAR UM TRANSPORTE')
            print('Digite o número correspondente das cidades de \npartida e destino, cidades disponíveis:'.center(55))
            print(formatar_cidades(cidades, 3))
            print(separador())
            partida = verif_int('Digite o número da cidade de partida: ')
            destino = verif_int('Digite o número da cidade de destino: ')
            if 0 <= partida and destino < len(cidades):
                print('Você selecionou da cidade de', cidades[partida], 'até', cidades[destino])
            else:
                print('Desculpe, uma das cidades que você digitou não está disponível ou não existe.')
            print(separador())
            print('Selecione o porte do caminhão a realizar o transporte:')
            lista_porte = ['Pequeno porte', 'Médio porte', 'Grande porte']
            print(formatar_cidades(lista_porte, 3))
            print(separador())
            porte = verif_int('Digite o número do porte do caminhão: ')
            distancia = matriz(lista_linhas, partida + 1, destino) # +1 pq a lista de linhas não começa do 0

            # definir preço do porte e multiplicar pela distancia para obter o custo

            if 0 <= porte < len(lista_porte):
                print(f'De {cidades[partida]} para {cidades[destino]}, utilizando um caminhão de {lista_porte[porte].lower()}, a distância é de {distancia}km e o \n custo de R$')
            else:
                print('Por favor, digite uma opção válida de porte') 
            #criar opções de voltar para o menu ou recomeçar
        case 2:
            cabeçalho('CADASTRAR UM TRANSPORTE') 
        # VER OUTRAS OPÇÕES DE IMPLEMENTAÇÃO
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

            
        case 3:
            cabeçalho('REGISTRO DE TRANSPORTES')
            ler_registro(registro)
            
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

       
