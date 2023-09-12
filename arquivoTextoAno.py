from datetime import datetime

# Função para gerar o próximo mês e ano
def proximo_mes_ano(data):
    data_obj = datetime.strptime(data, '%m-%Y')
    novo_mes = data_obj.month + 1
    novo_ano = data_obj.year

    if novo_mes > 12:
        novo_mes = 1
        novo_ano += 1

    return f'{novo_mes:02d}-{novo_ano}'

# Abra o arquivo de entrada para leitura
with open(r'C:\Users\Clayton.Roquini\PycharmProjects\VPN\esteTXT.txt', 'r') as arquivo_entrada:
    linhas = arquivo_entrada.readlines()

# Crie uma lista para armazenar as novas linhas
novas_linhas = []

# Repita o processo x vezes
for _ in range(10):
    # Processamento das linhas
    for i, linha in enumerate(linhas):
        partes = linha.strip().split(';')
        if len(partes) >= 2:
            if i == 0 or partes[0] == '1':  # Ignorar a segunda coluna da primeira linha  quando o primeiro campo for '1'
                novas_linhas.append(linha)
                continue

            data_atual = partes[1]
            while data_atual != '12-2023':
                novo_mes_ano = proximo_mes_ano(data_atual)
                partes[1] = novo_mes_ano
                nova_linha = ';'.join(partes) + '\n'
                novas_linhas.append(nova_linha)
                data_atual = novo_mes_ano

    # Verifique se a última linha não é a última do arquivo
    if not linhas[-1].strip().endswith('12-2023;'):
        partes = linhas[-1].strip().split(';')
        partes[1] = '12-2023'
        nova_linha = ';'.join(partes) + '\n'
        novas_linhas.append(nova_linha)

# Abra o arquivo de saída para escrita e escreva as novas linhas
with open(r'C:\Users\Clayton.Roquini\PycharmProjects\VPN\Arqnovo.txt', 'w') as arquivo_saida:
    arquivo_saida.writelines(novas_linhas)
