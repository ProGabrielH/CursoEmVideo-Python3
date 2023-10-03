# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições

from datetime import date

def voto(a):
    idade = date.today().year - a
    if idade < 18:
        return "Voto Negado"
    elif idade > 65:
        return "Voto Opcional"
    else:
        return "Voto Obrigatório"

print(voto(int(input('Digite seu ano de nascimento: '))))
