import random

minusculas = 'abcdefghijklmnopqrstuvwxyz'
maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
simbolos = '[](){}/.,;_-'

tudo = minusculas + maiusculas + simbolos
tamanho = 20

senha = ''.join(random.sample(tudo, tamanho))


for i in range(10):
    senha = ''.join(random.sample(tudo, tamanho))
    print(senha)
