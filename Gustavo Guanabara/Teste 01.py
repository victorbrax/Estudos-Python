venda = float
lucro = float
valfim = float

venda = input("Digite o valor da venda: ")

if venda <= 1000:
    lucro = 0.2
elif venda > 1000:
    lucro = 0.15

valfim = venda + venda * lucro

print("O valor final deve ser de: ",valfim)