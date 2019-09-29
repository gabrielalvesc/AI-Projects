import re
from collections import Counter

# texto = open("sherlock.txt").read()

# Lemos todas as palavras do testo e as dividimos
def palavras(texto):
    return re.findall(r'\w+', texto.lower())

#Contams quantas vezes as palavras aparecem para que possamos usar de sugerir a palavra com maior probabilidade
def counter_palavras():
    return Counter(palavras(open('shakespeare.txt').read()))
