# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
# exista la dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem.

lista = []

while True:
    num = int(input('Digite um número: (999 para encerrar) '))
    if lista.count(num) > 0:
        print('Número já inserido')
    elif num != 999:
        lista.append(num)
    else:
        break
print(sorted(lista))
