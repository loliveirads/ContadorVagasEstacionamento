import os

# Caminho para o diretório que contém o arquivo
file_path = r'C:\Users\luizf\OneDrive\visao_computacional_dev_ideias\Contador_vagas'

# Listar todos os arquivos no diretório
arquivos = os.listdir(file_path)
print("Arquivos no diretório:", arquivos)

# Verificar se 'vagas.pkl' está no diretório
file_name = 'vagas.pkl'
full_path = os.path.join(file_path, file_name)

if file_name in arquivos:
    print(f"O arquivo {full_path} existe.")
else:
    print(f"O arquivo {full_path} não existe.")
