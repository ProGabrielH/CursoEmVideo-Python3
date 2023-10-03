# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência
# de Fibonacci
n1, n2 = 0, 1
termos = int(input('Digite quantos termos você deseja ver: '))
count = 0

while count < termos:
    print(n1, end=' ')
    nn2 = n1 + n2
    n1 = n2
    n2 = nn2
    count += 1

# Usando loop for

#for i in range(0,termos):
#    print(n1, end=' ')
#    nn2 = n1 + n2
#    n1 = n2
#    n2 = nn2
