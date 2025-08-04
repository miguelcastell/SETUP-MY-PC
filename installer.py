import subprocess
import os

print("\nAguarde as instalações via winget...")

apps = [
    ("Google Chrome", "winget install --id=Google.Chrome -e --silent"),
    ("Java JDK", "winget install --id=Oracle.JDK -e --silent"),
    ("Java JRE", "winget install --id=Microsoft.OpenJDK.17 -e --silent"),
    ("Winrar", "winget install --id=Rarlab.WinRAR -e --silent"),
    ("Adobe Acrobat Reader", "winget install --id=Adobe.Acrobat.Reader.64-bit -e --silent"),
    ("AnyDesk", "winget install --id=AnyDesk.AnyDesk -e --silent"),
]

local_installers = [
    ("Assinador Serpro", "AssinadorSERPRO4.2.1.exe", "/S"),
    ("Danfe View", "nInstalador.exe", "/silent"),
]

def instalar_apps():
    for nome, cmd in apps:
        print(f"Instalando {nome}...")
        subprocess.run(cmd, shell=True)
        print(f"{nome} instalado!")

def instalar_exes_locais():
    for nome, arquivo, parametro in local_installers:
        caminho = os.path.join(os.path.dirname(__file__), arquivo)
        if os.path.exists(caminho):
            print(f"Instalando {nome}...")
            subprocess.run([caminho, parametro], check=True)
            print(f"{nome} instalado.")
        else:
            print(f"⚠️ Arquivo {arquivo} não encontrado!")

def criar_pastas():
    pastas = ["Projetos", "GitHub", "Ferramentas"]
    for p in pastas:
        caminho = os.path.join(os.path.expanduser("~"), p)
        os.makedirs(caminho, exist_ok=True)
        print(f"Pasta {p} criada em {caminho}")

if __name__ == "__main__":
    instalar_apps()
    criar_pastas()
    instalar_exes_locais()
    print("\nConfiguração concluída! Reinicie o computador se necessário.")
