def separador(tamanho = 60): # cria uma função de rodapé visual
    return '=' * tamanho


def cabeçalho(titulo): # cria uma função de cabeçalho visual para título
    print(separador())
    print(titulo.center(60))
    print(separador())


# verifica um numero inteiro e caso ocorra um erro de tipo, valor ou interrupção 
# do terminal pede o número novamente até ser inteiro
def verif_int(resposta): 
  while True: 
      try:
          num_int = int(input(resposta))
      except(ValueError, TypeError):
            cabeçalho("Por favor, digite um número inteiro válido.")
            continue
      except KeyboardInterrupt:
          print('Nenhum número digitado')
          return False
      else:
         return num_int
      

def verif_float(resposta): 
  while True: 
      try:
          num_float = float(input(resposta))
      except(ValueError, TypeError):
            cabeçalho("Por favor, digite um número real (float) válido. (1; 1.0; 1.5)")
            continue
      except KeyboardInterrupt:
          print('Nenhum número digitado')
          return False
      else:
         return num_float


# cria um menu numerado com a quantidade de opções de uma lista 
def menu(lista, titulo):
    cabeçalho(titulo)
    num = 1
    for item in lista:
        print(f'[{num}] - {item}')
        num += 1
    print(separador())
    opc_do_usuario = verif_int('Digite uma opção: ')
    return opc_do_usuario

# verifica se existe um arquivo para registro no repositório
def verificar_registro(registro):
    try:
        abrir = open(registro, 'rt')
        abrir.close()
    except FileNotFoundError:
        return False
    else:
        return True


# cria um arquivo para registro no repositório
def criar_registro(registro):
    try:
        abrir = open(registro, 'wt+')
        abrir.close()
    except:
        print('Não foi possível criar um registro')
    else:
        print('Registro criado')


# verifica se é possível abrir o arquivo
def ler_registro(registro):
    try:
        abrir = open(registro, 'rt')
    except:
        print('Não foi possível ler a tabela')
    else:
        print(abrir.read())


# retorna a distancia de uma matriz das cidades do arquivo CSV
# lista de listas
# a = indice da cidade linha INT +1
# b = distancia, que esta no indice cidade coluna INT
def matriz(lista, a, b):
    dist = lista[a][b]
    return dist



# cria um loop para enumerar todas cidades com seu indice em uma string
# da a opção de escolher quantas cidades vão por linha no terminal
def formatar_cidades(cidades, cidades_por_linha):
    string_cidades = ''
    for i, cidade in enumerate(cidades):
        string_cidades += f'[{i}] - {cidade}, '
        if (i+1) % cidades_por_linha == 0: # caso sobrar cidades, remover a ultima vírgula e quebrar a linha
            string_cidades = string_cidades.rstrip(', ')
            string_cidades += '\n'
    string_cidades = string_cidades.rstrip(', \n')
    return string_cidades


