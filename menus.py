def separador(tamanho = 42): # cria uma função de rodapé visual
    return '=' * tamanho


def cabeçalho(titulo): # cria uma função de cabeçalho visual com título
    print(separador())
    print(titulo.center(42))
    print(separador())


def verif_int(msg):
  while True: 
      try:
          n = int(input(msg))
      except(ValueError, TypeError):
            print("Por favor, digite uma opção válida.")
            continue
      else:
         return n


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    opc_do_menu = 1
    for item in lista:
        print(f'[{opc_do_menu}] - {item}')
        opc_do_menu += 1
    print(separador())
    opc_do_usuario = verif_int('Digite uma opção: ')
    return opc_do_usuario









