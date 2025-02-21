import os
valor_venda: list = []

with open(file='./carros.csv', mode='r', encoding='utf8') as arquivo:
    linha = arquivo.readline()  # lê o cabeçalho
    linha = arquivo.readline()  # lê a primeira linha
    while linha:
        # quebra a string nas virgulas e salva os resultados em uma lista
        linha_separada = linha.split(sep=',')

        # seleciona o segundo elemento da lista
        segundo_elemento = linha_separada[1]

        # salva o valor na lista de valor_venda
        valor_venda.append(segundo_elemento)

        # lê uma nova linha, se a linha não existir, salva o valor None
        linha = arquivo.readline()

    print(valor_venda)

###

    # leia o arquivo com o comando 'with' utilizando o parametro 'nome_arquivo'
    # O caminho para o arquivo deve começar com '../../data/'
    # extraia a coluna do arquivo utilizando o parametro 'indice_coluna'

"""
def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int):
    coluna: list = []
    with open(file=f'../../data/{nome_arquivo}', mode='r', encoding='utf8') as arquivo:
        arquivo.readline()
        for linha in arquivo:
            linha_separada = linha.strip().split(',')

            if len(linha_separada) > indice_coluna:
                coluna.append(linha_separada[indice_coluna])

        return coluna


valor_manutencao = extrai_coluna_csv(
    nome_arquivo='carros.csv',
    indice_coluna=2
)
print(valor_manutencao)
"""


###

# leia o arquivo com o comando 'with' utilizando o parametro 'nome_arquivo'.
# O caminho para o arquivo deve começar com '../../data/'
# extraia a coluna do arquivo utilizando o parametro 'indice_coluna'
# use a estrutura de decisão if/elif/else para fazer a conversão do tipo de dados utilizando o parametro 'tipo_dado'


def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int, tipo_dado: str):
    coluna: list = []

    try:
        if tipo_dado not in ["str", "int"]:
            raise ValueError(
                f"Parâmetro 'tipo_dado' invalido: {tipo_dado}. Aceitos: 'str' ou 'int'.")
    except ValueError as e:
        print(e)
        return []

    with open(file="./carros.csv", mode='r', encoding='utf8') as arquivo:
        arquivo.readline()

        for linha in arquivo:
            valores_linha = linha.strip().split(',')

            if len(valores_linha) > indice_coluna:
                valor_str = valores_linha[indice_coluna]

                if tipo_dado == "int":
                    try:
                        valor: int = int(valor_str)
                    except ValueError:
                        print(
                            f"Erro ao converter '{valor_str}' para inteiro. Pulando valor.")
                        continue
                    coluna.append(valor)
                else:
                    coluna.append(valor_str)

    return coluna


valor_manutencao = extrai_coluna_csv(
    nome_arquivo='carros.csv',
    indice_coluna=2,
    tipo_dado='str'
)

print(valor_manutencao)

###

# extraia a linha do arquivo utilizando o parametro 'numero_linha'


def extrai_linha_txt(nome_arquivo: str, numero_linha: int):

    palavras_linha: list = []

    try:
        with open(file=f'../../data/{nome_arquivo}', mode='r', encoding='utf8') as arquivo:
            # with open(file=f'./{nome_arquivo}', mode='r', encoding='utf8') as arquivo:

            for index, linha in enumerate(arquivo, start=1):
                if index == numero_linha:
                    palavras_linha = linha.split(' ')
                    # print(valores_linha)
                    break
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

    return palavras_linha


linha10 = extrai_linha_txt(nome_arquivo='musica.txt', numero_linha=5)
print(linha10)
