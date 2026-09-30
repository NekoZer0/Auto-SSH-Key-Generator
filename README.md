# Auto SSH Key & Config Generator (Python + OpenSSH)

Script em Python para geração e gerenciamento automatizado de múltiplas chaves SSH (`Ed25519`) em sistemas Linux, com atualização automática do arquivo `~/.ssh/config`.

## 🚀 Funcionalidades

* **Dinamismo total:** Identifica o diretório `Home` do usuário sem hardcode.
* **Múltiplas chaves:** Evita sobrescrever chaves existentes ao nomear os arquivos de acordo com o serviço/destino.
* **Configuração automática:** Adiciona a entrada correspondente diretamente no arquivo `~/.ssh/config`.
* **Permissões de segurança:** Garante permissões adequadas de pasta (`700`) e arquivos (`600`) exigidas pelo SSH.
* **100% Nativo:** Utiliza apenas módulos padrão do Python (`os`, `subprocess`) e o `ssh-keygen` do sistema.

---

## 📌 Pré-requisitos

* **Sistemas Linux / WSL / macOS**
* **OpenSSH Client** instalado (padrão na maioria das distribuições)
* **Python 3.x**

---

## 💻 Como Usar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   cd seu-repositorio