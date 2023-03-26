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




### ÁREA DO MENU VISUAL ###

from menus import *
import pandas as pd # Para manipulação de dados do arquivo CSV nas funções do sistema


distancias = pd.read_csv('DNIT-distancias.csv', sep=';') # Lê o arquivo csv

menu_principal = menu(['Consultar um Transporte', 'Cadastrar um Transporte', 'Registro de Cadastros', 'Encerrar Sessão'])
print(menu_principal)
