while True:
    palavra = ['Perfume', 'Bandeira', 'Camiseta', 'Geladeira', 'Computador']

    def verificador(x):
        try:
            x = int(x)
        except:
            print("Digite apenas números.")
            print()

    def maximo(x):
        if x <= 0 or x > 4:
            print("Digite apenas números entre 1 e 4")
            print()

    chances = input('Digite quantas chances você quer (no máximo 4): ')
    verificador(chances)
    chances = int(chances)
    if chances > 4:
        print('Penalidade aplicada!')
        condition = 0
        segredo = 5

    if condition == 1:
        segredo = input("Escolha um número para a palavra (no máximo 4): ")
        verificador(segredo)
        segredo = int(segredo)
        maximo(segredo)


    # letra = input('Digite uma letra: ')

    # if letra in len(palavra[segredo]):
    #     print('BOA')



