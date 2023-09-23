# Crie um programa que leia uma frase qualquer e diga se ela é um palídromo, desconsiderando espaços

print('IDENTIFICADOR DE PALÍDROMO')
frase = input('\nDigite uma frase: ').replace(' ', '')
frase_invertida = frase[::-1]

if frase == frase_invertida:
    print('É um palídromo')
else:
    print('Não é um palídromo')
