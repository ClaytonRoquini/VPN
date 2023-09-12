import os
import datetime
from win32api import GetFileVersionInfo, LOWORD, HIWORD

def obter_versao_data_dll(caminho_dll):
    # Obtém a versão do arquivo da DLL
    info = GetFileVersionInfo(caminho_dll, "\\")
    versao = HIWORD(info['FileVersionMS']), LOWORD(info['FileVersionMS']), HIWORD(info['FileVersionLS']), LOWORD(info['FileVersionLS'])

    # Obtém a data de modificação do arquivo da DLL
    data_modificacao = datetime.datetime.fromtimestamp(os.path.getmtime(caminho_dll))

    return versao, data_modificacao

# Especifique o caminho das duas DLLs que deseja comparar
dll1 = r"C:\PRODEMONSTRATIVO.DLL"
dll2 = r"C:\Windows\SysWOW64\PRODEMONSTRATIVO.DLL"

# Obtém informações da primeira DLL
versao_dll1, data_dll1 = obter_versao_data_dll(dll1)

# Obtém informações da segunda DLL
versao_dll2, data_dll2 = obter_versao_data_dll(dll2)

# Exibe as informações das DLLs
print("DLL 1:")
print("Versão:", ".".join(map(str, versao_dll1)))
print("Data de modificação:", data_dll1)

print("\nDLL 2:")
print("Versão:", ".".join(map(str, versao_dll2)))
print("Data de modificação:", data_dll2)

# Comparação das versões
if versao_dll1 > versao_dll2:
    print("\nDLL 1 é uma versão mais recente do que DLL 2.")
elif versao_dll1 < versao_dll2:
    print("\nDLL 2 é uma versão mais recente do que DLL 1.")
else:
    print("\nAs DLLs têm a mesma versão.")

# Comparação das datas de modificação
if data_dll1 > data_dll2:
    print("A DLL 1 foi modificada mais recentemente do que a DLL 2.")
elif data_dll1 < data_dll2:
    print("A DLL 2 foi modificada mais recentemente do que a DLL 1.")
else:
    print("As DLLs foram modificadas na mesma data.")
