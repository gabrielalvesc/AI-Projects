import sugestor
import re
import teste

print("OBS: The sentence must be at least 3 words.")
frase = input("Write a sentence: ")
frase_split = re.findall(sugestor.regex, frase.lower())

if len(frase_split) >= 3:
    response = teste.exists(frase_split)

    if(len(response) == 1):
        print("Right words: "+response[0].upper())
    else:
        
        texto = ''
        for t in response[2]:
            texto += t+' '

        texto += str(response[1]).upper()
        print("\n"+"Wrong word: "+texto+"\n")
        print("***** Sugestões de palavras *****\n")
        sugestoes = ""
        for s in response[0]:
            sugestoes += s+"    "
        print(sugestoes)

else:
    print("The sentence must be at least 3 words.")
