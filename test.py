
# distancias = csv.reader('DNIT-distancias.csv', sep=';') # Lê o arquivo csv



# cidades = lista_linhas[0] # Uma lista de nomes de cidades
#linhas = lista_linhas # Uma lista de listas


'''nome_cidade = 1 # X posição da cidade
linha_cidade = 1 # Y posição 
matriz = (linhas[nome_cidade])[linha_cidade] # MATRIZ!!!
matriz'''

import csv

with open('DNIT-distancias.csv', 'r') as tabela:
    ler = csv.reader(tabela, delimiter=';')
    lista_linhas = list(ler)

def matriz(a, b):
    dist = (lista_linhas[a])[b]
    print(dist)
    return dist
x = int(input('digite a '))
y = int(input('digite b '))
matriz(x, y)






