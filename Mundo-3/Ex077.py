# Crie um programa que  tenha uma tupla com várias palavras. Depois disso, você deve mostrar, para cada palavra, quais
# são suas vogais.

palavras = ('PALAVRA', 'PYTHON', 'CURSO', 'PROGRAMACAO', 'ARROZ', 'MONITOR', 'TECLADO', 'CPU', 'RYZEN', 'AMD', 'NVIDIA'
            , 'AMOR', 'LINDA')
for i in palavras:
    print(f'\nNa palavra {i} temos as vogais: ', end='')
    for letra in i:
        if letra.lower() in 'aeiouy':
            print(letra, end=' ')
