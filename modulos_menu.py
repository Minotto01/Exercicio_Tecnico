def separador(tamanho = 50): # cria uma função de rodapé visual
    return '=' * tamanho


def cabeçalho(titulo): # cria uma função de cabeçalho visual para título
    print(separador())
    print(titulo.center(50))
    print(separador())


def verif_int(resposta):
  while True: 
      try:
          num_int = int(input(resposta))
      except(ValueError, TypeError):
            cabeçalho("Por favor, digite um número inteiro válido.")
            continue
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

