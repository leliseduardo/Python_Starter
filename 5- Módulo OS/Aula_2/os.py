import os

os.getcwd()     # Retorna caminho da pasta que está este arquivo

os.listdir('C:/Users/eleli/Documents')    # Retorna todos os arquivos dentro da mesma pasta deste arquivo
                                          # Arquivos com . são arquivos ocultos


os.chdir()      # Troca diretório deste arquivo

os.mkdir('Pasta2') # Cria pasta

os.rename('teste.txt', 'teste2.txt') # Troca nome de arquivo qualquer

os.remove('teste.csv') # Remove arquivo, menos pastas

os.rmdir('pasta2') # Remove pastas

cmd = 'systeminfo'
os.system(cmd)