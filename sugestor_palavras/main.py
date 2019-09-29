import sugestor

sair = False

while(sair != True):
    print("\nEscolha dentre as opções abaixo:\n\n{1} Bigrama\n{2} Trigrama\n{X} Sair\n")
    opcao = input("Opção: ")

    if (opcao == '1'):
        print("\n********** Bigrama **********\n")
        print("OBS: A frase deve conter duas ou mais palavras.")
        frase = input("Digite a frase: ")
        frase_split = frase.split(" ")
        
        print("\nCarregando...\n")
        sugestoes = sugestor.sugestoes_bigrama(frase_split)
        print("Sugestões para o bigrama: ")
        for i in range(len(sugestoes)):
            print(frase+" "+sugestoes[i])

        continue
    elif (opcao == '2'):
        print("\n********** Trigrama **********\n")
        print("OBS: A frase deve conter três ou mais palavras.")
        frase = input("Digite a frase: ")
        palavras_frase = sugestor.re.findall(sugestor.regex, frase.lower())
        
        print("\nCarregando...\n")
        sugestoes = sugestor.sugestoes_trigrama(palavras_frase)
        print("Sugestões para o trigrama: ")
        for i in range(len(sugestoes)):
            print(frase+" "+sugestoes[i])

        continue
    elif (opcao == 'X' or opcao == 'x'):
        print('Até mais!!!')
        sair = True
    else:
        print('Opção inválida')
        continue
