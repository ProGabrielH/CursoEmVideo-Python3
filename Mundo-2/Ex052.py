# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
results = []

for i in range(1,n+1):
    if n % i == 0:
        results.append(i)
print(f'{n} é divisível por: ', results)
if len(results) > 2:
    print(f'{n} não é numero primo')
else:
    print(f'{n} é um número primo')
