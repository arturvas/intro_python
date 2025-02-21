idades = []
# read m2a1
with open(file='./banco.csv', mode='r', encoding='utf-8') as arquivo:
    linha = arquivo.readline()  # lê o cabeçalho
    linha = arquivo.readline()  # lê a primeira linha
    while linha:
        linha_separada = linha.split(sep=',')
        idade = linha_separada[0]
        idades.append(idade)
        linha = arquivo.readline()

# m2a2 2.2
# write
with open(file='idades.csv', mode='w', encoding='utf-8') as fp:
    linha = 'idade' + '\n'
    fp.write(linha)
    for idade in idades:
        linha = str(idade) + '\n'
        fp.write(linha)

# modo add
with open(file='idades.csv', mode='a', encoding='utf-8') as fp:
    for idade in idades:
        linha = str(int(idade) + 100) + '\n'
        fp.write(linha)

# copy a file with other extension
with open(file='./banco-text.txt', mode='r', encoding='utf8') as read:
    with open(file='./banco-csv.csv', mode='w', encoding='utf8') as write:
        line = read.readline()
        while line:
            write.write(line)
            line = read.readline()
