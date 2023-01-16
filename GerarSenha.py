import random

minusculas = '[abcdefghijklmnopqrstuvwxyz]'
maiusculas = minusculas.upper()
simbolos = '._-@*#$%'

tudo = minusculas + maiusculas + simbolos
tamanho = 20


for i in range(10):
    senha = ''.join(random.sample(tudo, tamanho))
    print(senha)
