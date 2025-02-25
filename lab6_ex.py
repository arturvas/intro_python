class ArquivoTexto(object):
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.conteudo = self.extrair_conteudo()

    def extrair_conteudo(self):
        conteudo = list()
        with open(f"data/{self.arquivo}", "r") as arquivo:
            conteudo = arquivo.readlines()
        return [linha for linha in conteudo]

    def extrair_linha(self, numero_linha: int):
        numero_linha -= 1
        if numero_linha < 0 or numero_linha >= len(self.conteudo):
            return None
        return self.conteudo[numero_linha]


musica = ArquivoTexto("musica.txt")
# print(musica.conteudo)


# licao 2

import sys

sys.path.insert(0, "data")


class ArquivoCSV(ArquivoTexto):

    def __init__(self, arquivo: str):
        super().__init__(arquivo=arquivo)
        self.colunas = self.extrair_nome_colunas()

    def extrair_nome_colunas(self):
        primeira_linha = self.conteudo[0]
        if (primeira_linha, list):
            return primeira_linha
        return primeira_linha.strip().split(",")

    def extrair_coluna(self, indice_coluna: int):
        indice_coluna -= 1
        coluna = list()
        for linha in self.conteudo[1:]:
            coluna.append(linha.strip().split(",")[indice_coluna])
        return coluna


arquivo = ArquivoCSV("arquivo-csv.csv")
print(arquivo.conteudo)
print(arquivo.colunas)
print(arquivo.extrair_coluna(2))
print(arquivo.extrair_linha(2))
print(arquivo.extrair_linha(3))

arquivo_pessoa = ArquivoCSV("info-pessoas.csv")

education = arquivo_pessoa.extrair_coluna(3)
print(education)
