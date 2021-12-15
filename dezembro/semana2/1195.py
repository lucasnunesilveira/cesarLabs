tamanho = int(input(""))
if 1 < tamanho < 1000:
    x = input("").split(" ")
    list(x)
    menor_numero = min(x)
    for k, i in enumerate(x):
        if i == menor_numero:
            print(f"Menor valor: {menor_numero}")
            print(f"Posicao: {k}")
