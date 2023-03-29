from modulos import * # importei o modulo menu do repositorio com * para não precisar digitar menu. antes de cada função
from time import sleep
import csv

with open('DNIT-distancias.csv', 'r') as tabela:
    ler = csv.reader(tabela, delimiter=';')
    lista_linhas = list(ler)

# lista com as cidades
cidades = lista_linhas[0]

while True: # loop para implementar funções as opções do menu
    menu_principal = menu(['Consultar um Transporte', 'Cadastrar um Transporte', 'Registro de Transportes', 'Encerrar Sessão'], 'MENU PRINCIPAL')
    match menu_principal:
        case 1: 
            def consulta():
                cabeçalho('CONSULTAR UM TRANSPORTE') # titulo

                print('Digite o número correspondente das cidades de \npartida e destino, cidades disponíveis:'.center(60))

                print(formatar_cidades(cidades, 3)) # função que mostra todas opções de cidades com seu indice
                print(separador())
                valido = False
                while True:
                    try:
                        partida = verif_int('Digite o número da cidade de partida: ')
                        destino = verif_int('Digite o número da cidade de destino: ')
                        print(separador())
                        if 0 <= partida and destino < len(cidades): # se partida E destino estão dentro da lista cidades
                            print('Você selecionou da cidade de', cidades[partida], 'até', cidades[destino])
                            print(separador())
                            break
                        else:
                            print('Desculpe, uma das cidades que você digitou não está disponível ou não existe.')
                            continue
                    except IndexError:
                        print('Desculpe, uma das cidades que você digitou não está disponível ou não existe.')
                        continue
            
                print('Selecione o porte do caminhão a realizar o transporte:')
                lista_porte = ['PEQUENO porte', 'MÉDIO porte', 'GRANDE porte']
                preço_porte = [4.87, 11.92, 27.44] # preço por km rodado
                print(formatar_cidades(lista_porte, 3))
                print(separador())
                porte_válido = False
                while not porte_válido:
                    porte = verif_int('Digite o número do porte do caminhão: ')
                    distancia = matriz(lista_linhas, partida + 1, destino) # +1 pq a lista de linhas não começa do 0

                    print(separador())
                    
                    if 0 <= porte < len(lista_porte):
                        cabeçalho(f'De {cidades[partida]} para {cidades[destino]}, utilizando um caminhão de \n{lista_porte[porte].lower()}, a distância é de {distancia}km e o custo de R${int(distancia)/preço_porte[porte]:.2f}'.center(60))
                        porte_válido = True
                    else:
                        print('Por favor, digite uma opção válida de porte.') 
                        print(separador())    
                
            consulta()
            sleep(1)
            mini_menu1 = menu(['Voltar ao menu principal', 'Fazer uma nova consulta', 'Encerrar sessão'], 'O QUE DESEJA FAZER AGORA?')
            match mini_menu1:
                case 1:
                    continue
                case 2:
                    consulta()
                    sleep(1)
                case 3:
                    confirm = input('Tem certeza que deseja sair? (S/N) ').lower()
                    if confirm == 's':
                        cabeçalho('Que pena! Até logo, volte sempre!')
                        break
                    elif confirm == 'n':
                        continue
                    else: # caso o usuario digite algo diferente de 's' ou 'n'
                        valido = False
                        while not valido: #loop continua em quanto for diferente de 's' ou 'n'
                            confirm2 = input('Não entendi, por favor digite (S/N): ').lower()
                            match confirm2: 
                                case 's':
                                    cabeçalho('Que pena! Até logo, volte sempre!')
                                    break
                                case 'n':
                                    valido = True
                                case outro:
                                    valido = False
                        if  confirm2 == 's': # se confirm2 for 's' fecha o programa
                            break
                        else: # se for 'n' reinicia
                            continue


        case 2:
            certeza_registro = menu(['Sim', 'Não, voltar'], 'DESEJA CADASTRAR UM TRANSPORTE?')
            match certeza_registro:
                case 1:
                    # verifica se existe o arquivo registro, se não existir cria o arquivo no repositório
                    registro = 'tabela_registro.csv'
                    if not verificar_registro(registro):
                        criar_registro(registro)
                    def registrar():
                        cabeçalho('CADASTRAR UM TRANSPORTE') 
                        # receber 2 ou mais cidades e 1 ou mais itens, responder o trajeto total e caminhão mais adequado
                        # custo por trecho e total
                        sleep(0.5)

                        # MOSTRAR CIDADES DISPONÍVEIS
                        valido = False
                        while not valido:
                            n_cidades = verif_int('Por favor, digite o número total de cidades do trajeto: ')
                            if n_cidades <= 1:
                                print('Por favor use pelo menos DUAS cidades...')
                                continue
                            else:
                                break
                        print('Estas são as cidades disponíveis: ')
                        print(formatar_cidades(cidades, 3))
                        print(separador())                   
                        
                        origem_indice = verif_int('Digite o número correspondente da cidade de ORIGEM: ')
                        trajeto_do_cadastro = []
                        trajeto_do_cadastro.append(cidades[origem_indice]) # coloca a origem no indice 0 

                        for i in range(1, n_cidades): # pede o numero da proxima cidade 'n_cidade menor origem[0]' vezes
                            cidades_restantes = verif_int('Digite o número correspondente da próxima cidade: ')
                            trajeto_do_cadastro.append(cidades[cidades_restantes])

                        # LEVAR O TRAJETO DO CADASTRO PARA A TABELA_REGISTRO
                        #  informações dentro do registro (isso eu posso deixar no main e puxar do registro)
                        
                        # abre o arquivo do registro e escreve uma linha com uma  string vazia
                        with open('tabela_registro.csv', 'w', newline='') as tabela_registro:

                            # escreve no arquivo item peso e quantidade como Header do csv
                            cabeçalho_registro = ['Trajeto', 'Cliente','Item', 'Peso', 'Quantidade']
                            registrar = csv.DictWriter(tabela_registro, fieldnames=cabeçalho_registro)

                            registrar.writeheader()

                            # variavel para identificar de quem é o transporte
                            # fora do loop para registrar varios itens no mesmo nome
                            cliente = input('Digite seu nome ou o nome da empresa que representa: ')
                            # loop para registrar os itens quantas vezes o usuário quiser
                            while True:
                                try:
                                    item = input('Digite o nome do item que deseja adicionar: ')
                                except:
                                    item == ''
                                peso = verif_float('Digite o valor do peso unitário do item em Kg: ')
                                quantidade = verif_int('Digite a quantidade a transportar: ')

                                # escreve a variavel na sua respectiva coluna
                                registrar.writerow({'Trajeto': trajeto_do_cadastro, 'Cliente': cliente,'Item': item, 'Peso': peso, 'Quantidade': quantidade})

                                continuar = menu(['Sim, adicionar mais um item', 'Não, finalizar registro'], 'Deseja registrar mais algum item ao transporte?')
                                match continuar:
                                    case 1: # continua o loop de adicionar itens
                                        continue
                                    case 2: # sai do registro
                                        break

                            #TODO volta aqui depois!!! adicionar opções finais
                        
                    registrar()
                        
                case 2: # volta para o menu
                    continue
        case 3:
            # verifica se existe o arquivo registro, se não existir cria o arquivo no repositório
            registro = 'tabela_registro.csv'
            if not verificar_registro(registro):
                criar_registro(registro)

            # abre o arquivo com with as para abrir, usar e fechar automaticamente;
            '''Usa o comando dictreader do csv e um loop para preencher a lista_trajetos 
               com as listas da coluna Trajetos da tabela_registro.csv, preenchendo a 
               função menu() com as opções sendo os trajetos registrados'''
            with open('tabela_registro.csv', 'r') as tabela_registro:
                leitura = csv.DictReader(tabela_registro, delimiter=',')
                lista_trajetos = []
                lista_cliente = []
                for col in leitura:
                    lista_cliente.append(col['Cliente'])
                
                menu_registro = menu(lista_cliente, 'REGISTRO DE TRANSPORTES')
                
                # mostrar registros numerados com todas informações que pede;
                # ler tabela registro se tabela_registro estiver vazia ou não existir
                # printar não há registros disponíveis criar registro? registrar() 

            break
        case 4:
            confirm = input('Tem certeza que deseja sair? (S/N) ').lower()
            if confirm == 's':
                cabeçalho('Que pena! Até logo, volte sempre!')
                break
            elif confirm == 'n':
                continue
            else: # caso o usuario digite algo diferente de 's' ou 'n'
                valido = False
                while not valido: #loop continua em quanto for diferente de 's' ou 'n'
                    confirm2 = input('Não entendi, por favor digite (S/N): ').lower()
                    match confirm2: 
                        case 's':
                            cabeçalho('Que pena! Até logo, volte sempre!')
                            break
                        case 'n':
                            valido = True
                        case outro:
                            valido = False
                if  confirm2 == 's': # se confirm2 for 's' fecha o programa
                    break
                else: # se for 'n' reinicia
                    continue
        case outro:
                 print(separador())
                 print('Por favor, digite uma opção existente...')
                 sleep(2)
      

       
