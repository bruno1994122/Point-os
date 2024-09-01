

import os
import time
import sys
import subprocess

def clor(url, diretorio_destino):
    try:
        # Comando para clonar o repositório
        comando = ['git', 'clone', url, diretorio_destino]
        # Executa o comando
        subprocess.run(comando, check=True)
        print(f'Repositório clonado com sucesso em {diretorio_destino}.')
    except subprocess.CalledProcessError as e:
        print(f'Erro ao clonar o repositório: {e}', file=sys.stderr)

def aco(duracao=5):
    animação = ['/', '|', '\\', '-']
    inicio = time.time()
    
    while time.time() - inicio < duracao:
        for frame in animação:
            sys.stdout.write(f'\r{frame}')
            sys.stdout.flush()
            time.sleep(0.1)  # Ajuste o tempo entre frames conforme necessário

# Executar a animação por 5 segundos

print("esse é um instalador.")
print("porfavor, use pip install colorama para instalar")
print("carregando.")
aco()
print("...")
print("instalando git..")
os.system("pkg install git")
clor("https://github.com/bruno1994122/Point-os.git", "datae")
