from collections import Counter
import re

texto = open('shakespeare.txt').read()

regex = "[a-zA-Z']+"
palavras = re.findall(regex, texto.lower())
palavras = palavras[:(len(palavras)//50)]

counter_palavras = Counter(palavras)

lista_palavras = list(counter_palavras)

# lista_palavras = texto.split(' ')

def bigrama(palavra1, palavra2):
    count_bigrama = 0
    for i in range(len(palavras)-1):
        if (palavra1 == palavras[i] and palavra2 == palavras[i+1]):
            count_bigrama += 1

    return count_bigrama


def probabilidade_bigrama(palavra1, palavra2):
    qtd_palavra1 = counter_palavras[palavra1]
    qtd_duas_palavras = bigrama(palavra1, palavra2)
    return qtd_duas_palavras/qtd_palavra1

# print(probabilidade_bigrama('you','are'))


def trigrama(palavra1, palavra2, palavra3):
    count_trigrama = 0
    for i in range(len(palavras)-1):
        if (palavra1 == palavras[i] and palavra2 == palavras[i+1] and palavra3 == palavras[i+2]):
            count_trigrama += 1

    return count_trigrama


def probabilidade_trigrama(palavra1, palavra2, palavra3):
    qtd_trigrama = trigrama(palavra1, palavra2, palavra3)
    qtd_bigrama = bigrama(palavra1, palavra2)
    try:
        return qtd_trigrama/qtd_bigrama
    except ZeroDivisionError:
        return 0

# print(probabilidade_trigrama('you','are','the'))


def melhor_palavra_bigrama(palavras, lista_palavras):
    maior_prob = 0
    index = 0
    for i in range(len(lista_palavras)):
        prob = probabilidade_bigrama(palavras[-1], lista_palavras[i])

        if (prob >= maior_prob):
            maior_prob = prob
            index = i

    return lista_palavras[index]


def sugestoes_bigrama(palavras):
    lista_sugestoes = []
    palavra = None
    lista_de_palavras = lista_palavras
    for i in range(3):
        if palavra is not None:
            lista_de_palavras.remove(palavra)

        palavra = melhor_palavra_bigrama(palavras, lista_de_palavras)

        if(str(palavra).startswith('b')):
            lista_sugestoes.append(palavra)

    return lista_sugestoes


def melhor_palavra_trigrama(palavras, lista_palavras):
    maior_prob = 0
    index = 0
    for i in range(len(lista_palavras)):
        prob = probabilidade_trigrama(palavras[-2], palavras[-1], lista_palavras[i])

        if (prob >= maior_prob):
            maior_prob = prob
            index = i

    return lista_palavras[index]


def sugestoes_trigrama(palavras):
    lista_sugestoes = []
    palavra = None
    lista_de_palavras = lista_palavras
    for i in range(3):
        if palavra is not None:
            lista_de_palavras.remove(palavra)

        palavra = melhor_palavra_trigrama(palavras, lista_de_palavras)

        lista_sugestoes.append(palavra)

    return lista_sugestoes
