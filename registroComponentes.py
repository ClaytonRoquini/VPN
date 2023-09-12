import winreg

def is_dll_registered(dll_name):
    try:
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, "") as reg_key:
            num_subkeys = winreg.QueryInfoKey(reg_key)[0]
            for i in range(num_subkeys):
                subkey_name = winreg.EnumKey(reg_key, i)
                if subkey_name.lower().startswith(dll_name.lower()):
                    return True
    except FileNotFoundError:
        pass
    return False

dll_names = ["WKBCTB010100.DLL", "WkbTelaBarraProgresso.dll", "ProSql20.DLL"]


for dll_name in dll_names:
    if is_dll_registered(dll_name[:-4]):
        print(f"Uma subchave que começa com '{dll_name}' foi encontrada em HKEY_CLASSES_ROOT.")
    elif is_dll_registered("vbp"+ dll_name[:-4]):
        print(f"Uma subchave que começa com '{dll_name}' foi encontrada em HKEY_CLASSES_ROOT.")
    else:
        print(f"Nenhuma subchave que começa com '{dll_name}' foi encontrada em HKEY_CLASSES_ROOT.")
