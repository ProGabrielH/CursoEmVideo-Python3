# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção sem usar o sort. no final, mostre a lista ordenada na tela

lista = []

for i in range(0,5):
    n = int(input('Digite um número: '))
    if i == 0 or n >= lista[-1]:
        lista.append(n)
        print(f'Inserindo número na ultima posição')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Inserindo número na posição {pos}')
                break
            pos += 1
print('-='*30)
print(lista)
