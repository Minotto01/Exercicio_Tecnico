def separador(tamanho = 55): # cria uma função de rodapé visual
    return '=' * tamanho


def cabeçalho(titulo): # cria uma função de cabeçalho visual para título
    print(separador())
    print(titulo.center(55))
    print(separador())


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


def menu(lista, titulo):
    cabeçalho(titulo)
    num = 1
    for item in lista:
        print(f'[{num}] - {item}')
        num += 1
    print(separador())
    opc_do_usuario = verif_int('Digite uma opção: ')
    return opc_do_usuario


def verificar_registro(registro):
    try:
        abrir = open(registro, 'rt')
        abrir.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_registro(registro):
    try:
        abrir = open(registro, 'wt+')
        abrir.close()
    except:
        print('Não foi possível criar um registro')
    else:
        print('Registro criado')


def ler_registro(registro):
    try:
        abrir = open(registro, 'rt')
    except:
        print('Não foi possível ler a tabela')
    else:
        print(abrir.read())

def matriz(lista, a, b):
    dist = (lista[a])[b]
    return dist

matriz()

def formatar_cidades(cidades, cidades_por_linha):
    string_cidades = ""
    for i, cidade in enumerate(cidades):
        string_cidades += f"[{i}] - {cidade}, "
        if (i+1) % cidades_por_linha == 0:
            string_cidades = string_cidades.rstrip(", ")
            string_cidades += "\n"
    string_cidades = string_cidades.rstrip(", \n")
    return string_cidades