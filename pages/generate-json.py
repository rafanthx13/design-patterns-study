import os
import json

# Diretório atual
diretorio_atual = os.getcwd()

# Lista de arquivos HTML encontrados
arquivos_html = [arquivo for arquivo in os.listdir(diretorio_atual) if arquivo.endswith(".html")]

# Criar o dicionário com os arquivos HTML
arquivos_dict = {"arquivos": arquivos_html}

# Salvar o dicionário como JSON no arquivo files.json
with open("files.json", "w") as arquivo_json:
    json.dump(arquivos_dict, arquivo_json)

