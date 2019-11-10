# coding: utf-8

import random

alfa = [' ', 'f', 'ī', 'a', 'q', '#', 'Ŧ', 'ǯ', '¿', 'Ǆ', 'ƍ', '™', '®', 'Ġ', '0', 'ķ', 'L', 'Ā', 'O', 'Ə', 'ō', '&', 'ǡ', '³', 't', 'ă', 'Ǒ', '¹', 'Â', 'ď', 'Ǭ', '¶', 'ǜ', '`', 'Ǟ', 'ȁ', 'ţ', 'ƣ', 'ő', 'ǽ', 'Ț', 'ċ', 'ø', '–', 'ș', 'Ȕ', 'Ò', 'Ɖ', 'Ŭ', 'Ǯ', 'ȍ', 'ȟ', 'Ǉ', '€', 'ĩ', 'ĺ', 'Ļ', '”', 'Ɯ', 'Ī', 'ǳ', 'ę', 'ð', 'ơ', 'ƙ', 'Ű', '|', 'Ř', 'â', 'ŭ', 'ǀ', '1', 'è', '<', 'Ǔ', 'Ŋ', '‚', 'ż', 'Ă', '·', 'ã', '‡', '¾', '—', 'Ũ', 'Ĥ', 'Ȓ', 'ƻ', 'Ǻ', 'o', '7', '÷', 'Ɛ', '-', '«', 'Ô', 'Ǝ', 'Ţ', 'ƒ', 'd', 'Ƒ', 'ê', 'ƃ', 'Ʋ', 'ª', 'Ɗ', 'ˆ', 'ó', 'ĸ', '»', 'ƕ', 'ŉ', '¡', 'Ħ', 'š', 'ŕ', 'ú', 'Ɲ', '…', 'V', 'ȉ', 'Ȗ', 'J', 'Õ', 'Ņ', 'ȓ', 'Ȇ', ']', 'ŵ', 'ļ', 'Đ', '%', 'Ʒ', 'K', 'ŝ', 'ǧ', 'R', 'Ȃ', 'ǝ', 'Ǚ', 'Ï', "'", 'ǟ', 'Ś', 'ȗ', 'Ė', 'Ŀ', 'Ƶ', 'Æ', 'Ŕ', 'ņ', 'Ƕ', '¦', 'ŏ', 'ǥ', 'ǉ', 'Ǡ', 'į', 'ı', 'ý', 'ù', 'õ', 'ô', 'Û', 'B', '›', 'Á', 'ȝ', '8', 'º', 'Ñ', 'Ǿ', 'ŷ', 'Ȝ', 'Ŷ', 'ŋ', 'ä', 'Ƅ', '±', '´', 'Ķ', 'Ư', 'þ', 'ź', '’', 'ů', 'ƀ', 'æ', 'ư', 'Ǜ', 'Ƈ', 'ť', 'ň', 'Ü', 'Ƹ', 'ǐ', 'ȅ', 'i', 'È', 'ś', 'z', '?', 'œ', 'ǁ', 'ŧ', 'ğ', 'g', 'ǣ', 'á', 'Č', 'Ĵ', 'Ģ', 'Ö', '‹', 'ā', 'Ŵ', '5', 'h', 'Ō', 'ǋ', 'ģ', 'Ɣ', 'ƨ', 'Ɵ', 'Ä', 'F', 'ǭ', 'Ľ', 'ƅ', 'Ȋ', '*', 'Ǽ', 'Ǥ', 'ǆ', 'č', 'Ɔ', 'ƪ', 'N', 'Î', 'ž', ',', 'Ĳ', 'ǫ', 'ö', ';', 'Ʀ', '•', '"', 'ƹ', '2', 'Š', 'Ź', 'Ç', 'Ɩ', 'k', '_', 'Ÿ', 'ß', 'ƈ', 'ľ', 'ȋ', '=', 'Ǌ', 'ē', 'u', 'b', 'ȑ', '×', 'í', 'Ǎ', 'ƭ', 'ĭ', '½', 'E', 'ç', 'ć', 'ĵ', '¨', 'Ž', '3', 'å', 'T', 'Å', 'ĉ', 'Ș', 'ǹ', 'ȏ', 'ų', 'ì', '°', 'Ȁ', 'ï', 'Ǘ', '$', 'Ĝ', '¯', 'r', 'đ', 'ǈ', 'Ż', 'Ĕ', 'Ǵ', '9', 'l', 'm', 'ǩ', 'Ê', 'Ų', 'c', 'Ȟ', 'A', 'Ƙ', 'X', 'ħ', 'M', 'Í', 's', '²', 'à', 'ƴ', 'ȇ', 'ǻ', '‰', '4', '„', 'ǘ', 'î', 'ñ', 'Ʈ', '/', 'Ǖ', 'Ş', 'Ȑ', 'ƚ', 'Ơ', ')', 'ÿ', 'ƶ', '}', '¼', 'Ĭ', 'ƿ', 'Ď', 'p', 'ĳ', 'Ù', 'x', 'Ʊ', 'ş', 'P', 'Ǹ', 'Þ', 'Ő', '.', 'Ƿ', 'ƛ', 'S', 'Ƨ', 'Ë', '+', '!', 'Ą', 'Ã', '~', 'ą', 'é', 'Z', 'Ů', 'ſ', 'ǵ', 'Ȍ', 'ȕ', 'Ĺ', 'Ì', 'Ǐ', 'ƾ', '©', 'Ń', 'ǌ', '{', 'Ý', 'Ň', 'ǂ', 'Ƥ', 'Ȉ', 'Ŗ', 'Į', 'Ł', 'y', 'Ĩ', 'ƞ', 'U', 'Q', 'ě', 'I', 'ü', 'Y', 'ǎ', 'ĕ', '“', ':', '¢', 'Ć', 'ŗ', '¥', 'Ƭ', '˜', 'ń', 'ǅ', 'Ɨ', 'Ð', 'ũ', 'Ƴ', 'ƌ', 'ĥ', 'Ǣ', 'H', 'ű', '¬', '(', 'Ȏ', 'µ', 'e', '@', 'Ƽ', 'ƺ', '^', 'ł', 'Ǳ', 'ǿ', 'ǃ', 'û', 'Ť', '§', 'ū', 'ë', 'À', 'Ē', 'W', '[', 'ƥ', 'É', 'ŀ', 'Ø', 'Ǩ', 'ǚ', 'w', 'ĝ', '‘', 'Ƌ', 'ǰ', 'ȃ', 'ė', 'G', 'Ğ', 'C', 'Ƣ', 'D', '£', 'Œ', '>', '†', 'Ǫ', 'Ū', 'j', 'ǔ', 'İ', 'ƫ', 'Ʃ', 'Ƃ', 'Ú', 'ǒ', 'Ǧ', 'Ȅ', '¸', 'ř', 'ǖ', 'Ŏ', 'ǲ', 'Ě', 'ƽ', 'n', 'ġ', '6', 'Ę', 'Ɠ', 'Ŝ', 'Ĉ', 'ț', 'v', 'Ó', 'Ɓ', 'Ċ', '¤', 'ò', '']


entrada, modo, senha = '', 0, ''

#====================================================================================================================================================================

def linha():
    print('\n'*7)
    print('='*70)
    print('='*70)
    print('='*70)
    print('\n\n')

def inputs():

    global entrada, modo, senha

    linha()
    entrada = str(input('Digite o texto a ser convertido:\n\n'))

    linha()
    senha = str(input('Digite a senha para a conversão:\n\n'))

    linha()
    modo = int(input('Digite o modo de conversão:\n1 = Cifrar\n2 = Decifrar\n\n'))

def SenCon():
    
    saida1 = ''
    
    global senha, entrada

    
    senhaCon = senha + str(len(entrada))

    for A in senhaCon:
        saida1 += str(alfa.index(A))

    return saida1

def cifrar():

    global entrada, modo

    saida = []
    saida2 = ''
    n1 = 0

    if modo == 1:

        for A in entrada:
            n1 += int(random.randrange(0, 10000))
            saida.append(alfa.index(A) + n1)
            if n1 > 10000:
                n1 -= 10000

    
    elif modo == 2:

        for A in entrada:
            n1 += int(random.randrange(0, 10000))
            saida.append(alfa.index(A) - n1)
            if n1 > 10000:
                n1 -= 10000

    
    for A in saida:
        
        B = A
        while (B not in range(0, len(alfa))):
            
            if B > len(alfa)-1:
                
                B -= len(alfa)-1

            elif B < len(alfa)-1:

                B += len(alfa)-1

        saida2 += alfa[B]

    return saida2

#====================================================================================================================================================================

while True:
    
    for Z in range(1):

        entrada, modo, senha = '', 0, ''
        
        nen = 0 #erro entrada
        nse = 0 #erro senha
        nmo = 0 #erro modo
        nal = 0 #soma das 3 anteriores

        print('\n\n\n\n')
        print('-'*80)
        print('-'*35, 'Cipher 2', '-'*35)
        print('-'*80)

        
        #\\\\\\\\\\\\\ Verificação dos inputs /////////////
        
        try:
            inputs()

        except:
            print('Você fez algo de errado durante a introdução dos valores de entrada, tente novamente!!!')
            break

        for A in range(1):

            for A in entrada:
                if A not in alfa:
                    nen += 1

            if modo != 1 and modo != 2:
                nmo += 1

            for A in senha:
                if A not in alfa:
                    nse += 1

            nal = nen + nse + nmo

        if nal > 0:
            
            linha()
            print('Você fez algo de errado durante a introdução dos valores de entrada, tente novamente!!!')
            break

        #///////////// stupni sod oãçacifireV \\\\\\\\\\\\\

        
        random.seed(SenCon())

        linha()
        print('Resultado:  ||>> {} <<||'.format(cifrar()))
    
    linha()
    n9 = int(input('Deseja continuar?\n1 = Sim\n2 = Não'))

    if n9 == 2:
        break
