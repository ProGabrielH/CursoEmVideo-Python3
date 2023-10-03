# Crie um programa que lia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores

qnt = soma = flag = 0
vals = []

valor = int(input('Digite o primeiro valor: '))
soma += valor
qnt += 1
vals.append(valor)

while flag == 0:
    resp = int(input('Para continuar, digite 1. Para finalizar, digite 2: '))
    if resp == 1:
        valor = int(input('Digite o próximo valor: '))
        soma += valor
        qnt += 1
        vals.append(valor)
    else:
        flag = 1

vals.sort()
print(f'O maior valor foi {vals[-1]} \nO menor valor foi {vals[0]} \nA média dos valores foi {soma/qnt}')
