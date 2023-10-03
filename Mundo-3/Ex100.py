# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai colocálos dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função
# anterior
from random import randint

numeros = list()


def sorteia():
    for i in range(0, randint(5, 15)):
        numeros.append(randint(1, 20))
    print(f'Os números sorteados foram {numeros}')
def somaPar(list):
    soma = 0
    for i in list:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos pares é: {soma}')


sorteia()
somaPar(numeros)
