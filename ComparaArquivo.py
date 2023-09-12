import os
import difflib
import logging
from PyPDF2 import PdfReader

def find_difference_line(texto_padrao, texto_novo):
    # Usando a biblioteca difflib para encontrar a diferença no texto linha a linha
    d = difflib.Differ()
    diff = d.compare(texto_padrao.splitlines(), texto_novo.splitlines())

    # Encontrar a primeira linha com diferença
    for line in diff:
        if line.startswith('- ') or line.startswith('+ '):
            return line

    return None

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

def compare_pdfs(file_padrao_path, file_novo_path):
    # Extrair o texto dos arquivos PDF usando Apache PDFBox
    texto_padrao = extract_text_from_pdf(file_padrao_path)
    texto_novo = extract_text_from_pdf(file_novo_path)

    if texto_padrao != texto_novo:
        diff_line = find_difference_line(texto_padrao, texto_novo)
        if diff_line:
            linha_num = diff_line.split()[1]  # Pegar o número da linha que contém a diferença
            diff_context = difflib.context_diff(texto_padrao.splitlines(), texto_novo.splitlines(), n=2, lineterm='')
            diffs = [f"Diferença encontrada na linha {linha_num}:\n"]
            diffs.extend(diff_context)
            return ''.join(diffs)

    return None

def compare_and_log_pdfs(folder_padrao, folder_novo, folder_log):
    # Verificar se a pasta log existe, senão, criá-la
    if not os.path.exists(folder_log):
        os.makedirs(folder_log)

    # Configurar o logging para gravar no arquivo de log apenas as mensagens de nível INFO
    log_file = os.path.join(folder_log, 'log.txt')
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(message)s')  # Apenas a mensagem será exibida no log

    arquivos_padrao = os.listdir(folder_padrao)
    arquivos_novo = os.listdir(folder_novo)

    for arquivo_padrao in arquivos_padrao:
        for arquivo_novo in arquivos_novo:
            if os.path.basename(arquivo_padrao) == os.path.basename(arquivo_novo):
                result = compare_pdfs(os.path.join(folder_padrao, arquivo_padrao),
                                      os.path.join(folder_novo, arquivo_novo))
                if result is not None:
                    log_message = f"Diferenças encontradas no arquivo {arquivo_padrao}:\n{result}\n"
                    logging.info(log_message)
                else:
                    logging.info(f"Não foram encontradas diferenças no arquivo {arquivo_padrao}.")
                break
        else:
            logging.info(f"Arquivo {arquivo_padrao} não encontrado na pasta 'novo'.")

# Exemplo de uso:
pasta_padrao = 'C:\\Users\\Clayton.Roquini\\Documents\\ComparaArquivos\\Padrão'
pasta_novo = 'C:\\Users\\Clayton.Roquini\\Documents\\ComparaArquivos\\Novo'
pasta_log = 'C:\\Users\\Clayton.Roquini\\Documents\\ComparaArquivos\\log'

compare_and_log_pdfs(pasta_padrao, pasta_novo, pasta_log)
