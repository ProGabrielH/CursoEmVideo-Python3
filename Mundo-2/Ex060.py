# Faça um programa que lia um número qualquer e mostre seu fatorial

num = int(input('Digite um número: '))

for i in range(num-1, 0, -1):
    num = num * i

print(f'Seu fatorial é:', num)