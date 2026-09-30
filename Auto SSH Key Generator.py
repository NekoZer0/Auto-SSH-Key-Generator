import os
import subprocess

def gerar_chave_ssh():
    # 1. Identifica dinamicamente o diretório Home do usuário atual
    home_dir = os.path.expanduser("~")
    ssh_dir = os.path.join(home_dir, ".ssh")
    
    # Garante que a pasta ~/.ssh exista com as permissões corretas (700)
    os.makedirs(ssh_dir, mode=0o700, exist_ok=True)

    # 2. Entrada de dados do usuário
    servico = input("Digite o identificador/serviço (ex: github_trabalho, servidor_prod): ").strip().lower().replace(" ", "_")
    email = input("Digite o e-mail para associar à chave: ").strip()
    hostname = input("Digite o HostName/IP (ex: github.com ou 192.168.1.100) [Padrão: github.com]: ").strip() or "github.com"
    usuario_ssh = input("Digite o usuário do SSH (ex: git ou root) [Padrão: git]: ").strip() or "git"

    if not servico or not email:
        print(" Erro: O identificador do serviço e o e-mail são obrigatórios.")
        return

    # Nome único para os arquivos da chave
    nome_chave = f"id_ed25519_{servico}"
    caminho_chave = os.path.join(ssh_dir, nome_chave)

    # Verifica se a chave já existe para evitar sobrescrevê-la
    if os.path.exists(caminho_chave):
        print(f" Erro: Já existe uma chave no caminho '{caminho_chave}'. Escolha outro nome de serviço.")
        return

    # 3. Executa o ssh-keygen
    cmd = [
        "ssh-keygen",
        "-t", "ed25519",
        "-C", email,
        "-f", caminho_chave,
        "-N", ""  # Passphrase vazia
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"\nChave SSH gerada com sucesso em: {caminho_chave}")
        print(f"Chave pública: {caminho_chave}.pub")
    except subprocess.CalledProcessError as e:
        print(f"Falha ao gerar a chave SSH: {e}")
        return

    # 4. Atualiza automaticamente o arquivo ~/.ssh/config
    caminho_config = os.path.join(ssh_dir, "config")
    
    bloco_config = f"""
# Configuração automatica para {servico}
Host {servico}
    HostName {hostname}
    User {usuario_ssh}
    IdentityFile {caminho_chave}
    IdentitiesOnly yes
"""

    with open(caminho_config, "a") as f:
        f.write(bloco_config)

    # Ajusta as permissões do arquivo de config para 600 (padrão de segurança do SSH)
    os.chmod(caminho_config, 0o600)

    print(f"Entrada adicionada com sucesso no arquivo '{caminho_config}'!")
    print("\n--- Como usar ---")
    if hostname == "github.com":
        print(f"• Para testar no GitHub, adicione o conteúdo do arquivo '{nome_chave}.pub' no GitHub e execute:")
        print(f"  ssh -T git@{servico}")
    else:
        print(f"• Para conectar no seu servidor, basta executar:")
        print(f"  ssh {servico}")

if __name__ == "__main__":
    gerar_chave_ssh()