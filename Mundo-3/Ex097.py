# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável

def escreva(msg):
    t = len(msg)+2
    print('~'*t)
    print(f' {msg:} ')
    print('~' * t)


msg = input('Mensagem pra ser digitada: ').strip()
escreva(msg)
