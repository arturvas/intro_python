from random import random
from functools import reduce


numeros = [round(100 * random()) for _ in range(0, 100)]
print(numeros)

numeros_ao_quadrado = map(lambda numero: numero ** 2, numeros)
print(list(numeros_ao_quadrado))  # retorna a referencia do objeto

numeros_impares = filter(lambda numero: numero % 2, numeros)
print(numeros_impares)  # retorna a referencia do objeto

soma_numeros = reduce(lambda x, y: x + y, numeros_impares)
print(soma_numeros)  # executa o calculo de fato

soma_numeros = reduce(lambda x, y: x + y, filter(lambda numero: numero %
                      2 != 0, map(lambda numero: numero ** 2, numeros)))
print(soma_numeros)
