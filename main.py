''' 
  TODO funções:
  # nota: o indice da linha que tem o valor ZERO é a cidade daquela linha
  # linha é uma lista
  # criar def caminhão
  # criar def menu
  # TRATAMENTO DE STRING nos inputs das cidades
    # Real com vírgula
    # nome em maísculo ou minúsculo, espaços, acentos, 
  # chamar os menus() dentro das match cases de resposta
    
  
  TODO implementações:
  1 [Consultar trechos x modalidade]
        -INPUT: nome de duas cidades e a modalidade(porte);
        -OUTPUT: distancia, custo total, se cidade não existir avisar;
        -EXEMPLO: (de PORTO ALEGRE para SÃO PAULO, utilizando um caminhão 
                   de pequeno porte, a distância é de XXX km e o custo 
                   será de R$ xxx,00.)

  2 [Cadastrar transporte, itens e pesos]
        -INPUT: uma sequência de cidades, itens e pesos
        -OUTPUT: distancia total, modelo mais custo-benefício e custos
        -EXEMPLO: (de PORTO ALEGRE para SÃO PAULO, a  distância 
            a ser percorrida é de X km, para transporte dos produtos X, Y , Z 
            será necessário utilizar 2 caminhões de porte PEQUENO e um de porte 
            MÉDIO, de forma a resultar no menor custo de transporte por km rodado. 
            O valor total do transporte dos itens é R$ xxx,00, sendo R$ xxx,00 é o 
            custo unitário médio.)

  3 [Dados estatísticos]
        -OUTPUT: exibir um relatório dos transportes cadastrados, para cada transporte 
        apresentar: CUSTO TOTAL; CUSTO POR TRECHO; CUSTO MÉDIO POR KM(TOTAL);
        CUSTO MÉDIO POR PRODUTO(CUSTO POR QUANTIDADE?); CUSTO TOTAL POR TRECHO; CUSTO TOTAL
        PARA CADA MODALIDADE; TOTAL DE VEÍCULOS; TOTAL DE ITENS, 
        se não ouver cadastros avisar
        # menu_transportes_cadastrados()  lista de informações 
'''


import pandas as pd # Para manipulação de dados do arquivo CSV nas funções do sistema


distancias = pd.read_csv('DNIT-distancias.csv', sep=';') # Lê o arquivo csv

### ÁREA DO MENU VISUAL ###

def separador(tamanho = 42): # cria uma função de rodapé visual
    return '=' * tamanho

def cabeçalho(titulo): # cria uma função de cabeçalho visual com título
    print(separador())
    print(titulo.center(42))
    print(separador())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    opção = 1
    for item in lista: # numera os itens da lista vezes o número de itens na lista
        print(f'[{opção}] - {item}')
        opção += 1


# decidi usar uma função que le uma lista e transofrma em menu para economizar tempo 
# e não escrever o menu a mão toda vez que tiver que usá-lo
menu_inicio = ['Consultar um Transporte', 'Cadastrar um Transporte', 'Registro de Cadastros', 'Encerrar Sessão']
menu(menu_inicio) 
print(separador())

### AREA DE RESPOSTA DO USUÁRIO ###



def resposta(num):
    match num: # match case para simplificar e diminuir quantidade de ifs 
            case 1: # Opção 1 CONSULTA
              print('Você escolheu a opção 1')

            case 2: # Opção 2 CADASTRO
              print('Você escolheu a opção 2')

            case 3: # Opção 3 REGISTRO
              print('Você escolheu a opção 3')

            case 4: # Opção 4 ENCERRAR SESSÃO
              confirmar_saida = input('Tem certeza que deseja sair? (S/N): ').lower()
              if confirmar_saida == 's':
                print(separador())
                print('Até logo, volte sempre!')
              elif confirmar_saida == 'n':
                menu(menu_inicio) 
                print(separador())
                resposta(int(input('Digite uma opção: ')))
                print(separador())
              else:
                print('Não entendi, digite uma opção válida! (S/N):')
            case outro:
              print(separador())
              print('ERRO: digite uma opção válida')
           
resposta(int(input('Digite uma opção: ')))
print(separador())

while True: 
    try:
        pass
    except ValueError:
          print("O valor deve ser um número inteiro")
    except KeyError:
          print("Opção inválida")




