# Desenvolva um programa que leia seis números inteiros e msotre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o
s = 0
for i in range(0,6):
    n = int(input('Digite um valor: '))
    if n%2 == 0:
        s += n

print(f'A soma dos desses valores pares é de: {s}')