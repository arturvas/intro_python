class ArquivoTexto(object):
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.conteudo = self.extrair_conteudo()

    def extrair_conteudo(self):
        conteudo = list()
        with open(f"/data/{self.arquivo}", "r") as arquivo:
            conteudo = arquivo.readlines()
        return [linha for linha in conteudo]

    def extrair_linha(self, numero_linha: int):
        numero_linha -= 1
        if numero_linha < 0 or numero_linha >= len(self.conteudo):
            return None
        return self.conteudo[numero_linha]


musica = ArquivoTexto("musica.txt")
print(musica.conteudo)


# licao 2

