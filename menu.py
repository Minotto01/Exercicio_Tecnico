def separador(tamanho = 42): # cria uma função de rodapé visual
    return '=' * tamanho


def cabeçalho(titulo): # cria uma função de cabeçalho visual para título
    print(separador())
    print(titulo.center(42))
    print(separador())


def verif_int(resposta):
  while True: 
      try:
          n = int(input(resposta))
      except(ValueError, TypeError):
            cabeçalho("Por favor, digite uma opção válida.")
            continue
      else:
         return n


def menu(lista, titulo):
    cabeçalho(titulo)
    num = 1
    for item in lista:
        print(f'[{num}] - {item}')
        num += 1
    print(separador())
    opc_do_usuario = verif_int('Digite uma opção: ')
    return opc_do_usuario


 
           




