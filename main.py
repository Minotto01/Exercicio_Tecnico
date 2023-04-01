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

                print(formatar_lista(cidades, 3)) # função que mostra todas opções de cidades com seu indice
                print(separador())
                valido = False
                while True:
                    try:
                        partida = verif_int('Digite o número da cidade de partida: ')
                        destino = verif_int('Digite o número da cidade de destino: ')
                        print(separador())
                        if partida == destino:
                            print('Desculpe, mas só fazemos transportes intermunicipais.')
                            print('Digite duas cidades diferentes.')
                            return True
                        elif 0 <= partida and destino < len(cidades): # se partida E destino estão dentro da lista cidades
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
                lista_porte = ['PEQUENO porte (Capacidade: 1 Tonelada)', 'MÉDIO porte (Capacidade: 4 Tonelada)', 'GRANDE porte (Capacidade: 10 Tonelada)']
                preço_porte = [4.87, 11.92, 27.44] # preço por km rodado
                print(formatar_lista(lista_porte, 1))
                print(separador())
                porte_válido = False
                while not porte_válido:
                    porte = verif_int('Digite o número do porte do caminhão: ')
                    distancia = matriz(lista_linhas, partida + 1, destino) # +1 pq a lista de linhas não começa do 0
                    print(separador())
                    if 0 <= porte < len(lista_porte):
                        print(f'De {cidades[partida]} para {cidades[destino]}, utilizando um caminhão de \n{lista_porte[porte].lower()}, a distância é de\n{distancia}km e o custo de R${int(distancia)/preço_porte[porte]:.2f}!'.center(60))
                        porte_válido = True
                    else:
                        print('Por favor, digite uma opção válida de porte.') 
                        print(separador())    
                
            consulta()
            print('Por Favor Aguarde')
            sleep(3)
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
                        print(formatar_lista(cidades, 3))
                        print(separador())                   
                        
                        origem_indice = verif_int('Digite o número correspondente da cidade de ORIGEM: ')
                        trajeto_do_cadastro = []
                        trajeto_do_cadastro.append(cidades[origem_indice]) # coloca a origem no indice 0 

                        for i in range(1, n_cidades): # pede o numero da proxima cidade 'n_cidade menor origem[0]' vezes
                            cidades_restantes = verif_int('Digite o número correspondente da PRÓXIMA cidade: ')
                            trajeto_do_cadastro.append(cidades[cidades_restantes])

                        
                        #  informações dentro do registro (isso eu posso deixar no main e puxar do registro)
                        
                        # abre o arquivo do registro e escreve uma linha com uma  string vazia
                        with open('tabela_registro.csv', 'w', newline='') as tabela_registro:

                            # escreve no arquivo item peso e quantidade como Header do csv
                            cabeçalho_registro = ['Trajeto', 'Cliente','Item', 'Peso', 'Quantidade']
                            registrar = csv.DictWriter(tabela_registro, fieldnames=cabeçalho_registro)
                            analisar_registro = csv.reader(tabela_registro)
                            registrar.writeheader()

                            # variavel para identificar de quem é o transporte
                            # fora do loop para registrar varios itens no mesmo nome
                            cliente = input('Digite SEU NOME ou o NOME DA EMPRESA que representa: ')
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
                                    case 2: # finalizar cadastro
                                        matrizes = []
                                        for i in range(len(trajeto_do_cadastro)-1):
                                            trajetos = [trajeto_do_cadastro[i], trajeto_do_cadastro[i+1]]
                                            matrizes.append(trajetos)
                                        distancias = []
                                        for i in range(len(matrizes)):
                                            trajeto = matrizes[i]
                                            y = trajeto[0]
                                            x = trajeto[1]
                                            distancia = matriz(lista_linhas, cidades.index(y) + 1, cidades.index(x))
                                            distancias.append(distancia)
                                            y = x      
                                        cabeçalho('REGISTRADO COM SUCESSO')
                                        numeros_inteiros = [int(numero) for numero in distancias]
                                        total = sum(numeros_inteiros)
                                        print(f'O trajeto do registro é: ')  
                                        print(formatar_lista(trajeto_do_cadastro, 3))
                                        print(f'A distância total a ser percorrida é {total}km.') 
                                        break
                                    case outro:
                                        cabeçalho('ERRO: opção inválida seu cadastro foi salvo, tente novamente')
                                        break
                    registrar()
                    mini_menu2 = menu(['Voltar ao menu principal', 'Encerrar sessão'], 'O QUE DESEJA FAZER AGORA?')
                    match mini_menu2:
                        case 1:
                            continue
                        case 2:
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
                case 2: # volta para o menu
                    continue
            continue
        case 3:
            # abre o arquivo com with as para abrir, usar e fechar automaticamente;
            try:
                with open('tabela_registro.csv', 'r') as tabela_registro:
                    leitura = csv.reader(tabela_registro)

                    for linhas in leitura:
                        print(linhas)
                    
                    continuar = menu(['Voltar ao menu', 'Encerrar sessão',], 'O que deseja fazer agora?')
                    match continuar:
                        case 1:
                            continue
                        case 2:
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
            except:
                print(separador())
                print('Ainda não há um registro para ser acessado'.center(60))
                continuar = menu(['Voltar ao menu', 'Encerrar sessão',], 'Volte ao menu para criar um registro')
                match continuar:
                    case 1:
                        continue
                    case 2:
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
      

       
