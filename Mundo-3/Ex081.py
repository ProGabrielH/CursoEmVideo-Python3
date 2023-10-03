# Crie um programa que vai ler vários números e colocar em uma lista. Depois mostre: 1- quantos números foram digitados
# 2- a lista de valores ordenada de forma decrescente. 3- se o valor 5 foi digitado na lista

vals = list()

while True:
    num = int(input('Digite um valor: [999 para finalizar] '))
    if num == 999:
        break
    else:
        vals.append(num)

print(f'Foram digitados {len(vals)} valores')
vals.sort(reverse=True)
print(f'A lista de forma decrescente: {vals}')
if vals.count(5) > 0:
    print(f'O valor "5" foi digitado {vals.count(5)} vezes')
else:
    print('O valor "5" não foi digitado')
