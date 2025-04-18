import os
import random

chances = 3
lista_palpites = []
ganhou = False
qtd_asteriscos = 50

def carregar_palavras(arquivo):
    dicionario = {}
    lista_tratada = []

    with open(arquivo, "r") as lista_palavras:
        for linha in lista_palavras:
            linha = linha.strip().split(';')
            lista_tratada.append(linha)
        for chave, valor in lista_tratada:
            if chave in dicionario.keys():
                dicionario[chave].append(valor)
            else:
                dicionario[chave] = [valor]

    return dicionario

def sortear_palavra(lista):
    tipo_palavra = random.choice(list(lista.keys()))
    palavra = random.choice(list(lista[tipo_palavra]))

    return tipo_palavra.upper(), palavra.upper()

def saudacao(asteriscos):
    texto_1 = f'BEM VINDO(A) AO JOGO DA FORCA!!!'
    texto_2 = f'BOA SORTE!!!'

    print(f"{'*' * asteriscos}")
    print(f"{'*' * asteriscos}")
    print(f"{'*' * asteriscos}")
    print(f"{texto_1:^{asteriscos}}")
    print(f"{'*' * asteriscos}")
    print(f"{'*' * asteriscos}")
    print(f"{texto_2:^{asteriscos}}")
    print(f"{'*' * asteriscos}")
    print(f"{'*' * asteriscos}")

def exibir_palavra(palavra, palpites, dica):
    print()
    print(f'A dica é:\t{dica}')
    for letra in palavra:
        if letra in palpites or letra == '-':
            print(letra.upper(), end = " ")
        else:
            print("_", end=" ")
    exibir_chutes(palpites)
    print()

def verificar_vitoria(palavra, palpites):
    for letra in palavra:
        if letra not in palpites:
            return False
    return True

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def msg_vitoria(palavra, asteriscos):
    texto_1 = f"PARABÉNS!!! VOCÊ ACERTOU!!!"
    texto_2 = f"A PALAVRA SECRETA ERA:\t{palavra}"

    print(f'{"*" * asteriscos}')
    print(f'{"*" * asteriscos}')
    print(f'{"*" * asteriscos}')
    print(f'{texto_1:^{asteriscos}}')
    print(f'{"*" * asteriscos}')
    print(f'{texto_2:^{asteriscos}}')
    print(f'{"*" * asteriscos}')
    print(f'{"*" * asteriscos}')
    input('\n\nPressione ENTER para continuar...')

def msg_derrota(palavra, asteriscos):
    texto_1 = f"VOCÊ PERDEU!!!"
    texto_2 = f"A PALAVRA SECRETA ERA:\t{palavra}"

    print(f'{"*" * asteriscos}')
    print(f'{"*" * asteriscos}')
    print(f'{"*" * asteriscos}')
    print(f'{texto_1:^{asteriscos}}')
    print(f'{"*" * asteriscos}')
    print(f'{"*" * asteriscos}')
    print(f'{texto_2:^{asteriscos}}')
    print(f'{"*" * asteriscos}')
    print(f'{"*" * asteriscos}')
    input('\n\nPressione ENTER para continuar...')

def exibir_chutes(lista):
    print('\nPalpites até agora:', end=' ')
    for chute in lista:
        print(f'{chute}', end = ' ')

lista_palavras = carregar_palavras("jogo_forca/lista.txt")
dica, palavra_secreta = sortear_palavra(lista_palavras)
while chances > 0 and not ganhou:
    limpa_tela()
    saudacao(qtd_asteriscos)

    print(f"\nTentativas restantes:\t{chances}")
    exibir_palavra(palavra_secreta, lista_palpites, dica)

    palpite = input(f"Digite uma letra:\t").upper()
    while palpite in lista_palpites:
        palpite = input(f"\nVocê já arriscou a letra '{palpite}'.\nDigite outra letra:\t").upper()
    lista_palpites.append(palpite)

    if palpite not in palavra_secreta:
        chances -= 1
        print(f'Você errou!\nA letra "{palpite}" não está na palavra')
        input('Pressione ENTER para continuar...')

    ganhou = verificar_vitoria(palavra_secreta, lista_palpites)

limpa_tela()
if ganhou:
    msg_vitoria(palavra_secreta, qtd_asteriscos)
else:
    msg_derrota(palavra_secreta, qtd_asteriscos)

limpa_tela()