# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. depois mostre: 1 Apenas os 5 preimeriso colocados. 2 Os 4 ultimos colocados. 3 uma lista com os times em
# ordem alfabética. 5 em que posição está o time Atlético-MG

times = ('BOTAFOGO', 'FLAMENGO', 'PALMEIRAS', 'GRÊMIO', 'FLUMINENSE', 'BRAGANTINO', 'ATHLETICO-PR', 'SÃO PAULO',
         'CUIABÁ', 'CRUZEIRO', 'FORTALEZA', 'INTERNACIONAL', 'ATLÉTICO-MG', 'CORINTHIANS', 'SANTOS', 'GOIÁS',
         'BAHIA', 'CORITIBA', 'AMÉRICA-MG', 'VASCO')
print(f'O tob 20 do Brasileirão: {times}')
print(f'Os 5 primeiros colocados são: {times[:5]}')
print(f'Os 4 ultimos colocados são: {times[16:]}')
print(f'Os times em ordem alfabética: {sorted(times)}')
print(f'O time "Atlético=MG" está na posição: {times.index("ATLÉTICO-MG")+1}')
