def escreve_arquivo_csv(nome: str, cabecalho: str, conteudos: list) -> bool:

    try:
        with open(file=nome, mode='w', encoding='utf8') as fp:
            linha = cabecalho + '\n'
            fp.write(linha)
            for conteudo in conteudos:
                linha = str(conteudo) + '\n'
                fp.write(linha)

    except Exception as exc:
        print(exc)
        return False

    return True


nome = 'idades-funcao-erro.csv'
cabecalho = 'idade'
conteudos = [10]

escreveu_com_sucesso = escreve_arquivo_csv(nome, cabecalho, conteudos)
print(f'Arquivo escreveu com sucesso? {escreveu_com_sucesso}')
