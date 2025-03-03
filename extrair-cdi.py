import os
import json
from random import random
from datetime import datetime

import requests

URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados?formato=json"

# Criando a variável data e hora

data_e_hora_atual = datetime.now()
data = datetime.strftime(data_e_hora_atual, "%Y/%m/%d")
hora = datetime.strftime(data_e_hora_atual, "%H:%M:%S")

# Captando a taxa CDI do site do BCB

try:
    response = requests.get(URL)
    response.raise_for_status()
except requests.HTTPError as exc:
    print("dado nao encontrado, continuando...")
    cdi = None
except Exception as exc:
    print("erro. parando a execucao...")
    raise exc
else:
    dado = json.loads(response.text)[-1]["valor"]
    cdi = float(dado) + (random() - 0.5)

# verificando se o arquivo existe

if os.path.exists("data/taxa_cdi.csv") == False:
    with open("data/taxa_cdi.csv", "w", encoding="utf8") as fp:
        fp.write("data,hora,taxa\n")

# salvando dados no arquivo "taxa-cdi.csv"

with open(file="data/taxa_cdi.csv", mode="a", encoding="utf8") as fp:
    fp.write(f"{data},{hora},{cdi}\n")

print("sucesso")
