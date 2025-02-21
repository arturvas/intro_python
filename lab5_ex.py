from functools import reduce
emprestimos = []
with open(file='./credito.csv', mode='r', encoding='utf8') as fp:
    fp.readline()  # cabeçalho
    linha = fp.readline()
    while linha:
        linha_emprestimo = {}
        linha_elementos = linha.strip().split(sep=',')
        linha_emprestimo['id_vendedor'] = linha_elementos[0]
        linha_emprestimo['valor_emprestimos'] = linha_elementos[1]
        linha_emprestimo['quantidade_emprestimos'] = linha_elementos[2]
        linha_emprestimo['data'] = linha_elementos[3]
        emprestimos.append(linha_emprestimo)
        linha = fp.readline()

# Escreva seu código abaixo

valor_emprestimos_map = map(lambda emprestimo: float(
    emprestimo['valor_emprestimos']), emprestimos)

valor_emprestimos_lista = list(valor_emprestimos_map)

print(valor_emprestimos_lista)


# -- licao 2 abaixo

valor_emprestimos_filtrado = filter(lambda x: x > 0, valor_emprestimos_lista)

valor_emprestimos_filtrado_lista = list(valor_emprestimos_filtrado)

print(valor_emprestimos_filtrado_lista)


# -- licao 3 abaixo

media_aritmetica = reduce(
    lambda x, y: x + y, valor_emprestimos_filtrado_lista) / len(valor_emprestimos_filtrado_lista)

print(media_aritmetica)


# -- licao 4 abaixo

quadrado_diferencas = map(lambda x: (x - media_aritmetica) ** 2, valor_emprestimos_filtrado_lista)

soma_quadrado_diferencas = reduce(lambda x, y: x + y, quadrado_diferencas)

desvio_padrao_emprestimos = (soma_quadrado_diferencas / (len(valor_emprestimos_filtrado_lista) - 1)) ** 0

print(desvio_padrao_emprestimos)
