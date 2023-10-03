# Faça um prorama que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno

def área(a, b):
    print(f'A área do quadrado {a}m por {b}m é {a*b:.1f}m')


altura = float(input('Digite a áltura: (m)'))
largura = float(input('Digite a largura: (m)'))

área(altura, largura)
