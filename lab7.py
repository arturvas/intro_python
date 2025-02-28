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

# ex 1, pandas

import pandas as pd

df = pd.read_csv("dados/dow_jones_index.csv")
print(df.head())

df.head(n=10)

df.columns.to_list()

linhas, colunas = df.shape
print(f"Linhas: {linhas}")
print(f"Colunas: {colunas}")

df_mcd = df[df["stock"] == "MCD"]
print(df_mcd)

df_mcd.head(n=10)
df_mcd.dtypes

for col in ["open", "high", "low", "close"]:
    df_mcd[col] = df_mcd[col].apply(lambda value: float(value.split(sep="$")[-1]))

df_mcd.head(n=10)
df_mcd.dtypes


# ex 2.1
import pandas as pd

df = pd.read_csv("dados/dow_jones_index.csv")

# Crie um Dataframe filtrado, selecionando as linha do dataframe original df em que a coluna stock é igual a KO.
df_coke = df[df["stock"] == "KO"]

# Selecione apenas as colunas de data e valores de ações: ['date', 'open', 'high', 'low', 'close'].
df_coke = df_coke[["date", "open", "high", "low", "close"]]
print(df_coke)

# Limpe as colunas com o método `apply`, que permite a aplicação de uma função anônima (`lambda`) qualquer. A função `lambda` deve remover o caracter `$` e fazer a conversão do tipo de `str` para `float`.

for col in df_coke.columns[1:]:
    df_coke[col] = df_coke[col].apply(lambda x: float(x.split("$")[-1]))

# print the types
print(df_coke.dtypes)

# ex 2.2

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

fig, axs = plt.subplots(1, figsize=(8, 8))
plt.xticks(rotation=45)
# Insira se código na linha abaixo. Veja a dica para resolver esse exercício
plot = sns.lineplot(data=df_coke, x="date", y="open", ax=axs)

plt.show()
