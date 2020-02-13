# coding: utf-8

from os import system
from cipherdef import cipher

entrada, modo, senha = '', 0, ''

def linha():
    print('\n'*2)
    print('='*70)
    print('='*70)
    print('\n\n')

def inputs():

    global entrada, modo, senha

    linha()
    entrada = str(input('Digite o texto a ser convertido:\n\n'))

    system('cls')
    linha()
    senha = str(input('Digite a senha para a conversão:\n\n'))

    system('cls')
    linha()
    modo = int(input('Digite o modo de conversão:\n1 = Cifrar\n2 = Decifrar\n\n'))

while True:
    
    for Z in range(1):

        entrada, modo, senha = '', 0, ''

        inputs()


        system('cls')
        linha()
        try:
            print('Resultado:  ||>>{}<<||'.format(cipher(entrada, senha, modo)))
        except Exception as erro:
            print(erro)


    linha()
    n9 = input('Deseja continuar?\n1 = Sim\n2 = Não')

    system('cls')

    if n9 == '2':
        break