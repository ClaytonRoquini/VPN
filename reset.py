import os, sys
import shutil
import tkinter as tk
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
#from ProgressBarWindow import ProgressBarWindow
import subprocess
import platform
import threading
import time
import ctypes
import datetime


def copiar_arquivo(origem, destino):
    if os.path.isdir(destino):
        shutil.rmtree(destino)  # Remove subpasta existente
    elif os.path.exists(destino):
        os.remove(destino)  # Remove arquivo existente

    if os.path.isdir(origem):
        shutil.copytree(origem, destino)
    else:
        shutil.copy2(origem, destino)


def copiar_arquivos_exe(pasta_origem, pasta_destino, titulo, desc):
    if not os.path.exists(pasta_origem):
        print(f"A pasta de origem '{pasta_origem}' não existe.")
        return

    try:
        total_arquivos = 0
        for root, dirs, files in os.walk(pasta_origem):
            for file in files:
                if file.lower().endswith('.exe'):
                    total_arquivos += 1

        progress_window = ProgressBarWindow(total_arquivos, titulo, desc)
        progresso = 0

        for root, dirs, files in os.walk(pasta_origem):
            for file in files:
                if file.lower().endswith('.exe'):

                    try:
                        caminho_origem = os.path.join(root, file)

                        # Cria o caminho de destino correspondente mantendo a estrutura de subpastas
                        subpasta_rel = os.path.relpath(root, pasta_origem)
                        caminho_destino = os.path.join(pasta_destino, subpasta_rel, file)

                        os.makedirs(os.path.dirname(caminho_destino), exist_ok=True)
                        shutil.copy2(caminho_origem, caminho_destino)
                        print(f"Arquivo Copiado: {caminho_origem}\n")
                    except Exception as e:
                        print(f"Erro ao Copiar Arquivo: {caminho_origem} - Erro: {str(e)}\n")
                        continue
                    progresso += 1
                    progress_window.update_progress(progresso)

        progress_window.destroy()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

        # messagebox.showinfo("Concluído", "Arquivos copiados para a pasta de destino com sucesso!")


def copiar_arquivos_outras_pastas(pasta_origem, pasta_destino, titulo, desc):
    if not os.path.exists(pasta_origem):
        print(f"A pasta de origem '{pasta_origem}' não existe.")
        return

    try:
        arquivos = os.listdir(pasta_origem)
        total_arquivos = len(arquivos)
        progresso = 0

        progress_window = ProgressBarWindow(total_arquivos, titulo, desc)

        # Data limite (01 de janeiro de 2020)
        data_limite = datetime.datetime(2020, 1, 1)

        desktop_dir = os.path.expanduser("~/Desktop")

        # Define o caminho completo para o arquivo de log
        log_file_path = os.path.join(desktop_dir, "log.txt")

        for arquivo in arquivos:
            origem = os.path.join(pasta_origem, arquivo)
            destino = os.path.join(pasta_destino, arquivo)

            # Verifique se o arquivo atende aos critérios de filtro
            data_criacao = datetime.datetime.fromtimestamp(os.path.getmtime(origem))

            nome_arquivo = os.path.basename(origem).lower()

            if (
                (data_criacao > data_limite  # Data de criação superior a 01 de janeiro de 2020
                 and nome_arquivo.startswith("pro"))  # Começa com "Pro"
                or nome_arquivo.startswith("wkb")  # Começa com "Wkb"
            ):
                try:
                    copiar_arquivo(origem, destino)
                    print(f"Arquivo Copiado: {origem}\n")
                except Exception as e:
                    print(f"Erro ao Copiar Arquivo: {origem} - Erro: {str(e)}\n")
                    continue

            progresso += 1
            progress_window.update_progress(progresso)

        progress_window.destroy()
        print("Concluído!")

    except Exception as e:
        print(f"Erro durante a cópia: {str(e)}")


def copiar_arquivos_outras_pastas_threaded(pasta_origem, pasta_destino):
    thread = threading.Thread(target=copiar_arquivos_outras_pastas, args=(pasta_origem, pasta_destino))
    thread.start()


def copiar_arquivos_recursivamente(pasta_origem, pasta_destino, titulo, desc):
    if not os.path.exists(pasta_origem):
        print(f"A pasta de origem '{pasta_origem}' não existe.")
        return

    files_to_copy = []
    for root, dirs, files in os.walk(pasta_origem):
        for file_name in files:
            if file_name.lower().endswith(('.dll', '.tlb')):
                files_to_copy.append(file_name)

    total_arquivos = len(files_to_copy)
    progress_window = ProgressBarWindow(total_arquivos, titulo, desc)
    progresso = 0
    for root, dirs, files in os.walk(pasta_origem):

        for file_name in files:
            if file_name.lower().endswith(('.dll', '.tlb')):

                try:
                    subpasta_origem = os.path.relpath(root, pasta_origem)
                    subpasta_origem_primeira = subpasta_origem.split(os.sep)[0]
                    pasta_destino_subpasta = os.path.join(pasta_destino, subpasta_origem_primeira)
                    os.makedirs(pasta_destino_subpasta, exist_ok=True)

                    origem = os.path.join(root, file_name)
                    destino = os.path.join(pasta_destino_subpasta, file_name)
                    shutil.copy2(origem, destino)
                    print(f"Arquivo Copiado: {origem}\n")
                except Exception as e:
                    print(f"Erro ao Copiar Arquivo: {origem} - Erro: {str(e)}\n")
                    continue

                progresso += 1
                progress_window.update_progress(progresso)

    progress_window.destroy()
    # messagebox.showinfo("Concluído", "Arquivos copiados para a pasta de destino com sucesso!")


def mapear_unidade_de_rede():
    usuario_remoto = "wkbrazil\\matheus.tavares"
    senha_remoto = "R3d44!eA"
    letra_unidade = "T:"
    caminho_compartilhado = r"\\172.14.10.22\Drive_F"

    comando = f'net use {letra_unidade} {caminho_compartilhado} /user:{usuario_remoto} {senha_remoto}'

    try:
        # Execute o comando usando subprocess
        resultado = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = resultado.communicate()

        # Verifique o resultado
        if resultado.returncode == 0:
            print(f"Unidade {letra_unidade} mapeada com sucesso para {caminho_compartilhado}")
        else:
            print(f"Erro ao mapear unidade de rede:\n{stderr.decode('utf-8')}")
    except Exception as e:
        print(f"Erro ao executar o comando 'net use': {e}")


def desmapear_unidade_de_rede():
    letra_unidade = "T:"
    try:
        # Execute o comando usando subprocess
        comando = f'net use {letra_unidade} /delete'
        resultado = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = resultado.communicate()

        # Verifique o resultado
        if resultado.returncode == 0:
            print(f"Unidade {letra_unidade} desmapeada com sucesso.")
        else:
            print(f"Erro ao desmapear unidade de rede {letra_unidade}:\n{stderr.decode('utf-8')}")
    except Exception as e:
        print(f"Erro ao executar o comando 'net use': {e}")


def selecionar_pasta_origem():
    global pasta_origem_var
    pasta_origem = filedialog.askdirectory()
    if pasta_origem:
        pasta_origem_var.set(pasta_origem)


def excluir_arquivo(arquivo):
    if os.path.exists(arquivo):
        os.remove(arquivo)


def get_system_architecture():
    arch = platform.architecture()[0]
    return arch


def configure_button_style():
    s = ttk.Style()
    s.configure('Custom.TButton', background='#25c0cf', foreground='white', font=('Helvetica', 12, 'bold'), height=30,
                widht=10)


def copiar_todos_os_arquivos():
    button_copiar_todos.config(state=tk.DISABLED)

    # Verificar se o script está sendo executado como administrador
    if not ctypes.windll.shell32.IsUserAnAdmin():
        # Se não for administrador, solicitar elevação de privilégios
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

    caminho_base_prosoft_win = r"C:\Prosoft.win"
    # caminho_base_remoto_prosoft_win = r"\\172.14.10.22\Drive_F\Fabrica\Engenharia\_Builds\VERSAO5\ServicePacks\DEVOPS\Prosoft.win"
    # caminho_base_remoto_prosoft_win = r"\\172.17.0.245\prosoft\Matheus\Reset de Componentes e Rotinas\Prosoft.win"
    # caminho_base_remoto_prosoft_win = r"\\172.18.0.30\Prosoft.win"
    caminho_base_remoto_prosoft_win = r"\\172.14.10.22\Drive_F\Fabrica\Engenharia\_Builds\VERSAO5\Instalador\Prosoft.win"
    caminho_base_patch = r"\\172.14.10.22\Drive_F\Fabrica\Engenharia\_Builds\VERSAO5\ServicePacks\DEVOPS\Prosoft.win"

    mapear_unidade_de_rede()

    pasta_origem_prGeral = caminho_base_remoto_prosoft_win + "\PrGeral"
    pasta_origem_patch_prGeral = caminho_base_patch + "\PrGeral"
    pasta_destino_prGeral = caminho_base_prosoft_win + "\PrGeral"

    pasta_origem_pcGold = caminho_base_remoto_prosoft_win + "\PcGold"
    pasta_origem_patch_pcGold = caminho_base_patch + "\PcGold"
    pasta_destino_pcGold = caminho_base_prosoft_win + "\PcGold"

    pasta_origem_scop_componentes = caminho_base_remoto_prosoft_win + "\SCOP\Componentes"
    pasta_origem_patch_scop_componentes = caminho_base_patch + "\SCOP\Componentes"
    pasta_destino_scop_componentes = caminho_base_prosoft_win + "\Scop\Componentes"

    pasta_destino_syswow = ""
    if get_system_architecture().startswith("64"):
        pasta_destino_syswow = r"C:\Windows\SysWOW64"
    else:
        pasta_destino_syswow = r"C:\Windows\system32"

    pasta_origem_componentes_net = caminho_base_remoto_prosoft_win + "\SCOP\Componentes.NET"
    pasta_origem_patch_componentes_net = caminho_base_patch + "\SCOP\Componentes.NET"
    pasta_destino_componentes_net = caminho_base_prosoft_win + "\Scop\Componentes.NET"

    pasta_destino_comp_dot_net_wolters = pasta_destino_syswow + "\CompDotNetWoltersKluwer"
    selvcomp_btr_path = caminho_base_prosoft_win + "\SELVCOMP.BTR"

    # copiar_arquivos_recursivamente(pasta_origem_componentes_net, pasta_destino_comp_dot_net_wolters, "SP - (1/6)", "Scop\Componentes.Net => SysWOW")
    # copiar_arquivos_exe(pasta_origem_prGeral, pasta_destino_prGeral, "SP - (2/6)", "PrGeral => PrGeral")
    # copiar_arquivos_outras_pastas(pasta_origem_scop_componentes, pasta_destino_scop_componentes, "SP - (3/6)", "Scop\Compontentes => Scop\Compontentes")
    # copiar_arquivos_outras_pastas(pasta_origem_scop_componentes, pasta_destino_syswow, "SP - (4/6)", "Scop\Compontentes => SysWOW")
    # copiar_arquivos_outras_pastas(pasta_origem_componentes_net, pasta_destino_componentes_net, "SP - (5/6)", "Scop\Componentes.Net => Scop\Componentes.Net")
    # copiar_arquivos_exe(pasta_origem_pcGold, pasta_destino_pcGold, "SP - (6/6)", "PcGold => PcGold")

    # copiar_arquivos_recursivamente(pasta_origem_patch_componentes_net, pasta_destino_comp_dot_net_wolters, "Patch - (1/6)", "Scop\Componentes.Net => SysWOW")
    # copiar_arquivos_exe(pasta_origem_patch_prGeral, pasta_destino_prGeral, "Patch - (2/6)", "PrGeral => PrGeral")
    # copiar_arquivos_outras_pastas(pasta_origem_patch_scop_componentes, pasta_destino_scop_componentes, "Patch - (3/6)", "Scop\Compontentes => Scop\Compontentes")
    # copiar_arquivos_outras_pastas(pasta_origem_patch_scop_componentes, pasta_destino_syswow, "Patch - (4/6)", "Scop\Compontentes => SysWOW")
    # copiar_arquivos_outras_pastas(pasta_origem_patch_componentes_net, pasta_destino_componentes_net, "Patch - (5/6)", "Scop\Componentes.Net => Scop\Componentes.Net")
    # copiar_arquivos_exe(pasta_origem_patch_pcGold, pasta_destino_pcGold, "Patch - (6/6)", "PcGold => PcGold")

    # excluir_arquivo(selvcomp_btr_path)

    # time.sleep(3)

    # messagebox.showinfo("Prosoft", "Cópia de Arquivos Concluída!")

    desmapear_unidade_de_rede()

    button_copiar_todos.config(state=tk.NORMAL)

    # prosoft_exe_path = r"C:\Prosoft.win\PROSOFT.exe"

    # subprocess.run(prosoft_exe_path)


window = tk.Tk()
window.title("Reset de Componentas e Rotinas")
window.geometry("300x150")
window.resizable(False, False)
# window.iconbitmap("./assets/favicon.ico")

frame_vertical = tk.Frame(window)
frame_vertical.pack(expand=True, fill="both")

frame_horizontal = tk.Frame(frame_vertical)
frame_horizontal.pack(expand=True)

style = {
    "background": "#211496",
    "foreground": "white",
    "font": ("Helvetica", 10, "bold"),
    "relief": "ridge",
    "bd": 4

}

button_copiar_todos = tk.Button(
    frame_horizontal,
    text="Resetar Componentes e Rotinas",
    **style,
    width=28,
    height=2,
    command=copiar_todos_os_arquivos
)



class ProgressBarWindow(tk.Toplevel):
    def __init__(self, max_value, title="Progresso", description="Copiando arquivos:"):
        super().__init__()
        self.title(f"Progresso {title}")
        self.geometry("300x100")

        self.progress_label = tk.Label(self, text=f"Copiando arquivos: \n{description}")
        self.progress_label.pack(pady=10)

        self.canvas_width = 200
        self.canvas_height = 20
        self.progress_canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.progress_canvas.pack(pady=10)

        self.progress_bar = self.progress_canvas.create_rectangle(0, 0, 0, self.canvas_height, fill="blue")

        self.max_value = max_value
        self.current_value = 0

    def update_progress(self, current_value):
        self.current_value = current_value
        if self.max_value != 0:
            progress_percentual = (self.current_value / self.max_value) * 100
        else:
            progress_percentual = 0

        self.progress_canvas.coords(self.progress_bar, 0, 0, (progress_percentual / 100) * self.canvas_width, self.canvas_height)
        self.update()

    def destroy(self):
        super().destroy()

    def run(self):
        self.update()
        self.mainloop()



def main():
    button_copiar_todos.pack(pady=10)

    if hasattr(sys, '_MEIPASS'):
        current_directory = sys._MEIPASS
    else:
        current_directory = os.path.dirname(os.path.abspath(__file__))

    # Definir o ícone da janela principal
    window.iconbitmap(os.path.join(current_directory, "assets", "favicon.ico"))

    frame_horizontal.grid_rowconfigure(0, weight=1)
    frame_horizontal.grid_columnconfigure(0, weight=1)

    frame_vertical.grid_rowconfigure(0, weight=1)

    window.mainloop()


main()
