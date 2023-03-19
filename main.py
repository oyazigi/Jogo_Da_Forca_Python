import random
import unidecode as un

def carregar_palavra():
    arquivo = open("palavras.txt", "r", encoding='utf-8')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()

        palavras.append(linha)

    arquivo.close()

    palavra_secreta = random.choice(palavras).upper()
    return palavra_secreta

resposta = carregar_palavra()
print(resposta)
resposta2 = un.unidecode(resposta)
palavra = []
tracos = 0
for linha in resposta:
    if(linha == "-"):
        palavra.append(linha)
        tracos = tracos + 1
    else:
        palavra.append("_")
print(tracos)
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def posicaoletra(string, char):
    pos = []
    for n in range(len(string)):
        if string[n] == char:
            pos.append(n + 1)
    return pos

print("\n*********************************")
print("Bem vindo ao jogo da Forca!")
print("*********************************\n")
print("A Sua palavra contém", len(resposta) - tracos, "letras")

print(palavra)
letras_restantes = len(resposta) - tracos
letras_chutadas = []
erros = 0
acertos = 0
while erros != 7:

    guess = input("Digite o seu chute ")
    chute = guess.upper()
    if (letras_chutadas.count(chute) > 0):
        print("você chutou uma letra repetida\n")
        continue
    else:
        letras_chutadas.append(chute)
    posicao = resposta2.find(chute)
    if (posicao == -1):
        print("A palavra não contém essa letra\n")
        erros += 1
        desenha_forca(erros)
    else:
        print("\nvocê chutou certo! essa letra esta na posição: {}".format(posicaoletra(resposta2, chute)))
        for n in posicaoletra(resposta2, chute):
            palavra[n - 1] = chute
            acertos = acertos + 1
        letras_restantes = letras_restantes - len(posicaoletra(resposta2, chute))
        for letra in palavra:
            if letra == "_":
                nao_acabou = True
        if nao_acabou:
            print(palavra)
    if (letras_restantes != 0):
        print("te restam {} tentativas de erro\n".format(7 - erros))
    else:
        if acertos == len(resposta2) - tracos:
            print("parabéns você ganhou o jogo!")
            print("a palavra original era:{}".format(resposta))
            break
if erros == 7:
    print("você perdeu o jogo!")

