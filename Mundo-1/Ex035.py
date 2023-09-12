# Crie um programa que receba o comprimento de 3 retas e informe se pode ser formado um triângulo com as mesmas.
l1 = float(input('Por favor informe o comprimento do primeiro lado do triangulo: '))
l2 = float(input('Por favor informe o comprimento do segundo lado do triangulo: '))
l3 = float(input('Por favor informe o comprimento do terceiro lado do triangulo: '))

lados = [l1, l2, l3]
lados.sort()

if lados[0] + lados[1] >= lados[2]:
    print('Pode ser formado um triângulo')
else:
    print('Não pode ser formado um triângulo')
