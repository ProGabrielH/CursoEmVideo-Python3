# melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
# ele disse que quer mostrar 0 termos

termo = 0
pnum = int(input('Qual o primeiro termo da PA: '))
razao = int(input('Qual a razão da PA: '))
amais = 10
totalt = 0

while amais != 0:
    totalt += amais
    while termo != totalt:
        print(pnum, end=' ')
        pnum += razao
        termo += 1
    amais = int(input('\nQuantos termos adicionais você deseja ver? '))
print('FIM')
