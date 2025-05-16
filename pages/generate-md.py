import os

# Lê o arquivo "files.txt"
with open("files.txt", "r") as file:
    lines = file.readlines()

# Cria um arquivo HTML para cada linha
for line in lines:
    # Remove quebras de linha e espaços extras
    line = line.strip()

    # Gera o título com a primeira letra maiúscula
    title = line.capitalize()

    # Cria o conteúdo do arquivo HTML
    html_content = """
# {title}

.

"""
    html_content = html_content.replace("{title}", title)

    # Cria um novo arquivo HTML com o título como nome
    filename = f"{title}.md"
    with open(filename, "w") as html_file:
        html_file.write(html_content)

    print(f"Arquivo {filename} criado com sucesso.")

print("Processo concluído.")

