# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: 1- quantas
# vezes apareceu o valor 0. 2- em que posição foi digitado o primeiro valor 3. 3- quais foram os números pares
valor1 = int(input('Digie um valor: '))
valor2 = int(input('Digie um valor: '))
valor3 = int(input('Digie um valor: '))
valor4 = int(input('Digie um valor: '))
tupla = valor1, valor2, valor3, valor4
pares = []

print(tupla)
print(f'O valor 0 apareceu {tupla.count(0)} vezes')
if tupla.index(3) == 0:
    print('O valor 3 não foi digitado')
else:
    print(f'O valor 3 apareceu na posição {tupla.index(3)}')
for i in tupla:
    if i % 2 == 0:
        pares.append(i)
print(f'Os valores pares inseridos foram: {pares}')
