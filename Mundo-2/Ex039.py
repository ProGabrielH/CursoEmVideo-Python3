# Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade: -Se ele ainda vai se
# alistar, -Se é a hora de se alistar, -Se já passou do tempo de alistamento. Seu programa também deve mostrar quanto
# tempo que ainda falta ou o que pasou do prazo.

from time import strftime

ano_atual = int(strftime("%Y"))
ano = int(input('Qual seu ano de nascimento? '))

if ano_atual - ano == 18:
    print('Você deve se alistar esse ano')
elif ano_atual - ano < 18:
    print('Você ainda tem que se alistar')
    print(f'Faltam {ano_atual - ano} anos para você precisar se alistar')
elif ano_atual - ano > 18:
    print('O prazo de se alistar já passou, é bom você ter se alistado')
