# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado, Equilátero,
# Isóceles ou Escaleno
l1 = float(input('Por favor informe o comprimento do primeiro lado do triangulo: '))
l2 = float(input('Por favor informe o comprimento do segundo lado do triangulo: '))
l3 = float(input('Por favor informe o comprimento do terceiro lado do triangulo: '))

lados = [l1, l2, l3]
lados.sort()

if lados[0] + lados[1] >= lados[2]:
    print('Pode ser formado um triângulo')
    if lados[0] == lados[1] and lados[1] == lados[2]:
        print('É formado um triângulo do tipo EQUILATERO')
    elif lados[0] == lados[1] and lados[0] != lados[2] or lados[2] == lados[0] and lados[2] != lados[1] or lados[1] ==\
            lados[2] and lados[1] != lados[0]:
        print('É formado um triângulo do tipo ISÓCELES')
    elif lados[0] != lados[1] and lados[1] != lados[2]:
        print('É formado um triângulo do tipo ESCALENO')
else:
    print('Não pode ser formado um triângulo')