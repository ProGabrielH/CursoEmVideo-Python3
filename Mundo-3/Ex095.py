# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador

gols = []
jogadores = list()
dados = {}

while True:
    dados['nome'] = str(input('Nome do jogador: ').strip())
    tot = int(input(f'Quantos jogos {dados["nome"]} jogou? '))
    for i in range(0, tot):
        gols.append(int(input(f'Gols na partida {i+1}: ')))
    dados['gols'] = gols[:]
    jogadores.append(dados.copy())
    gols.clear()
    dados.clear()
    while True:
        resp = input('Deseja continuar [S/N]: ').strip().upper()[0]
        if resp in 'SsNn':
            break
        else:
            print('Resposta inválida')
    if resp in 'Nn':
        break
print(f'{"cód":<4} {"Nome":<10} {"Gols":^10} {"tot":>4}')
print('-'*31)
for k in range(0, len(jogadores)):
    print(f'{k:<4} {jogadores[k]["nome"].capitalize():<10} {jogadores[k]["gols"]} {sum(jogadores[k]["gols"]):>4}')
print('-'*31)

resp = input('\nDeseja ver um jogador em específico? [S/N]: ').strip().upper()[0]
if resp in 'Ss':
    while True:
        num = int(input('Digite o código do jogador [999 para encerrar]: '))
        if num == 999:
            break
        print(jogadores[num])
