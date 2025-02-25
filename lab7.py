# from lab6_ex import *
# arquivo_banco_pacote = ArquivoCSV(arquivo="banco.csv")

import zipfile
import wget
import os

os.rename("dados/dow_jones_index.data", "dados/dow_jones_index.csv")
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00312/dow_jones_index.zip"
arquivo_zip = "dados.zip"

try:
    wget.download(url=url, out=arquivo_zip)
    print("Download finalizado com sucesso!")
except Exception as e:
    print(f"Erro ao baixar arquivo: {e}")

try:
    with zipfile.ZipFile(arquivo_zip, "r") as zip_ref:
        zip_ref.extractall(arquivo_zip.replace(".zip", ""))
    print("Arquivo descompactado com sucesso!")
except Exception as e:
    print(f"Erro ao descompactar arquivo: {e}")
