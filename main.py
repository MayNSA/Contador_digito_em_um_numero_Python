
numero = float(input("Digite o valor de n: "))

digito = float(input("Digite o valor de d: "))

num = numero
contador = 0

while numero != 0:
    resultado = numero % 10
    if resultado == digito:
        contador += 1
    numero = numero // 10

print("{} ocorre {} vezes em {}".format(digito, contador, num))
