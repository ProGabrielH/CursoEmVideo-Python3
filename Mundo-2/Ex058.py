# Melhore o jogo do 028 onde o computador vai  "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar
# advinhar até acertar, mostando no final quantos palpites foram necessários para vencer.
from random import randint

tentativas = 0
var = 1
numpc = randint(0,10)
numeros_errados = []

print('Pensei em um número de 0 a 10, qual você acha que foi?')

while var == 1:
    guess = int(input('Seu palpite: '))
    if guess in numeros_errados:
        print('Você já tentou esse número, tente novamente')
    elif guess != numpc:
        print('Errado, tente de novo')
        tentativas += 1
        numeros_errados.append(guess)
    else:
        print(f'Isso mesmo, o número é {numpc} e você errou {tentativas} vezes antes de acertar')
        var = 0
