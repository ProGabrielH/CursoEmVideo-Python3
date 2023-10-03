# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso. de zero á 20. Seu programa
# deverá ler um número pelo teclado (entre 0 e 20) e mostrará-lo por extenxo

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    posicao = int(input('Digite um número de 0 a 20: '))
    if posicao >= 0 and posicao <= 20:
        break
    else:
        print('Tente novamente!', end=' ')

print('Você digitou o número ', end='')
print(numeros[posicao])