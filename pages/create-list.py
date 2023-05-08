import os

# Diretório atual
diretorio_atual = os.getcwd()

# Lista de arquivos HTML encontrados
arquivos_html = [arquivo for arquivo in os.listdir(diretorio_atual) if arquivo.endswith(".html")]

# Exibir a lista de arquivos HTML entre colchetes como uma lista de strings
lista_strings = ', '.join(['"{}"'.format(arquivo) for arquivo in arquivos_html])
print('[{}]'.format(lista_strings))

