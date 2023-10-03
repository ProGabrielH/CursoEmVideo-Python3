# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles

c = s = 0

while True:
    num = int(input('Digite um número: [999 para fechar o programa] '))
    if num != 999:
        c += 1
        s += num
    else:
        break

print(f'A soma dos {c} números é igual a {s}')
