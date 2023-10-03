# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles

flag = 0
soma = 0
qnt = 0

print('Digite o valor 999 para finalizar o programa')
while flag == 0:
    n = int(input('Digite um valor: '))
    if n != 999:
        soma += n
        qnt += 1
    else:
        flag = 1
print(f'A soma dos {qnt} valores é de: {soma}')
