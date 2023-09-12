import os
import pdfplumber
import difflib
import logging

def listar_arquivos(caminho, extensao):
    arquivos = []
    for arquivo in os.listdir(caminho):
        if arquivo.endswith(extensao):
            arquivos.append(os.path.join(caminho, arquivo))
    return arquivos

def comparar_pdfs(arquivo_padrao_path, arquivo_novo_path):
    with pdfplumber.open(arquivo_padrao_path) as pdf_padrao, pdfplumber.open(arquivo_novo_path) as pdf_novo:
        if len(pdf_padrao.pages) != len(pdf_novo.pages):
            return False, None

        diffs = []
        for page_num in range(len(pdf_padrao.pages)):
            page_padrao = pdf_padrao.pages[page_num]
            page_novo = pdf_novo.pages[page_num]

            texto_padrao = page_padrao.extract_text()
            texto_novo = page_novo.extract_text()

            if texto_padrao != texto_novo:
                d = difflib.Differ()
                diff = d.compare(texto_padrao.splitlines(), texto_novo.splitlines())
                diffs.append(f"Diferença encontrada na página {page_num + 1}:\n" + '\n'.join(diff))

        return len(diffs) == 0, diffs

def diff_conteudo(arquivo_padrao_path, arquivo_novo_path, log_builder):
    _, diffs = comparar_pdfs(arquivo_padrao_path, arquivo_novo_path)
    if diffs:
        for diff in diffs:
            log_builder.append(diff).append("\n")

def compare_and_log_pdfs(folder_padrao, folder_novo, folder_log):
    # Verificar se a pasta log existe, senão, criá-la
    if not os.path.exists(folder_log):
        os.makedirs(folder_log)

    # Configurar o logging para gravar no arquivo de log
    log_file = os.path.join(folder_log, 'log.txt')
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    arquivos_padrao = listar_arquivos(folder_padrao, ".pdf")
    arquivos_novo = listar_arquivos(folder_novo, ".pdf")

    for arquivo_padrao in arquivos_padrao:
        for arquivo_novo in arquivos_novo:
            if os.path.basename(arquivo_padrao) == os.path.basename(arquivo_novo):
                try:
                    log_builder = []
                    sao_iguais, diffs = comparar_pdfs(arquivo_padrao, arquivo_novo)
                    if not sao_iguais:
                        log_builder.append("Arquivos diferentes: ").append(os.path.basename(arquivo_padrao)).append("\n")
                        log_builder.append("Diferenças encontradas:\n")
                        for diff in diffs:
                            log_builder.append(diff).append("\n")
                        log_builder.append("-------------------------------------------------------------------------\n")
                    else:
                        log_builder.append("Arquivos sem diferença: ").append(os.path.basename(arquivo_padrao)).append("\n")
                        log_builder.append("-------------------------------------------------------------------------\n")
                    log_resultado = "".join(log_builder)
                    logging.info(log_resultado)
                except Exception as e:
                    print("Erro ao comparar os arquivos PDF:", e)
                break

# Exemplo de uso:
pasta_padrao = 'C:\\Users\\Clayton.Roquini\\Documents\\ComparaArquivos\\Padrão'
pasta_novo = 'C:\\Users\\Clayton.Roquini\\Documents\\ComparaArquivos\\Novo'
pasta_log = 'C:\\Users\\Clayton.Roquini\\Documents\\ComparaArquivos\\log'

compare_and_log_pdfs(pasta_padrao, pasta_novo, pasta_log)
