# Crie um programa que gerencia o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas prtidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incuindo o total de gols feitos dudante o campeonato.

dicionario = dict()
tot = 0

dicionario['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
qnt = int(input('Número de jogos: '))

for i in range(0, qnt):
    dicionario[f'jogo{i+1}'] = int(input(f'Número de gols marcados no jogo {i+1}: '))
    tot += dicionario[f'jogo{i+1}']
print('=-'*15)
print(f'O jogador {dicionario["nome"]} fez um total de {tot} gols')
