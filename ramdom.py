import random

pares = range(2, 61, 2)
impares = range(1, 61, 2)

qtd_par = int(input('Número par: '))
qtd_impar = int(input('Número impar: '))

pares_sorteados = random.sample(pares, qtd_par)
impares_sorteados = random.sample(impares, qtd_impar)

sorteados = pares_sorteados + impares_sorteados
sorteados.sort()

print(sorteados)