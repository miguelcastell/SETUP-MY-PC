# SetupMyPC

Automatize a instalação de programas essenciais em um PC novo com Windows. Este projeto utiliza um script em PowerShell com `winget` para facilitar a configuração inicial, instalando os principais aplicativos e criando uma estrutura de pastas útil para desenvolvedores e usuários em geral.

---

## Funcionalidades

- Instalação automatizada de softwares como:
  - Google Chrome
  - Visual Studio Code
  - Office
  - Winrar
  - Assinador SERPRO
  - Quais você quiser, basta pegar o ID do winget e adiconar na lista.
  - Scripts organizados e fáceis de customizar

---

## Requisitos

- Sistema operacional: Windows 10 ou 11
- Ter o `winget` instalado (geralmente já vem nas versões atuais)
- Executar o PowerShell como administrador

---

## Como usar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/SetupMyPC.git
cd SetupMyPC
```

2. Abra o PowerShell como administrador

3. Execute o script principal:

```powershell
./install.ps1
```

---

## Extras

Você pode expandir ou personalizar o projeto como quiser:

- Edite a lista de aplicativos no `install.ps1`
- Crie outras pastas no `extras/folders-setup.ps1`
- Instale extensões do VSCode com `extras/vscode-extensions.ps1`
- Adicione configurações adicionais (ex: WSL, terminal, temas)

---

## Estrutura de Pastas Criada

- C:\Users\SeuNome\Projetos
- C:\Users\SeuNome\GitHub
- C:\Users\SeuNome\Ferramentas
