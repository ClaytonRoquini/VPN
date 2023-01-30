import random




def generate_pis():
    # Gerando os 9 primeiros dígitos aleatoriamente
    pis = str(random.randint(1000000000, 9999999999))

    # Calculando o dígito verificador
    total = 0
    weight = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(10):
        total += int (pis[i]) * weight[i]
    rest = 11 - (total % 11)
    if rest == 10 or rest == 11:
        rest = 0
    pis += str(rest)
    return pis


# Chamando a função para gerar um PIS válido
print(generate_pis())


