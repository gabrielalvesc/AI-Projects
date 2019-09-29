import re
import regex
from collections import Counter
import sugestor

# Contamos a a quantidade de vezes que a palavra aparece pra usarmos essa probabilidade
counter_palavras = regex.counter_palavras()

def exists(palavras):
    
    palavras_aux = []
    for p in palavras:
        palavras_aux.append(p)

    lista_set = set(p for p in palavras if p in counter_palavras)
    print(lista_set)
    lista = list(lista_set)
    # print(lista, palavras)
    if(len(lista) == len(palavras)):
        frase = ""
        for f in palavras:
            frase+=f+" "
        return [frase]
    else:
        print("Carregando sugestões...")
        for i in range(len(lista)):
            palavras_aux.remove(lista[i])
        
        aux = []
        
        for p in palavras:
            if (p == palavras_aux[0]):
                break
            else:
                aux.append(p)
        
        return sugestor.sugestoes_trigrama(aux), palavras_aux[0], aux
