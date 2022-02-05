import random
resposta = carregar_palavra()
def gerar_palavra():
    global palavra
    palavra = random.choice(resposta)
    return palavra
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
            pos.append(n+1)
    return pos

def carregar_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()

        palavras.append(linha)

    arquivo.close()

    palavra_secreta = random.choice(palavras).upper()
    return palavra_secreta

print("\n*********************************")
print("Bem vindo ao jogo da Forca!")
print("*********************************\n")
print("A Sua palavra contém" , len(gerar_palavra()) , "letras")

letras_restantes = len(palavra)
letras_chutadas = []
erros = 0
while erros != 7:

    chute = input("Digite o seu chute ")
    if (letras_chutadas.count(chute) > 0):
        print("você chutou uma letra repetida\n")
        continue
    else:
        letras_chutadas.append(chute)
    posicao = palavra.find(chute)
    if(posicao == -1):
        print("A palavra não contém essa letra\n")
        erros += 1
        desenha_forca(erros)
    else:
       print("\nvocê chutou certo! essa letra esta na posição: {}".format(posicaoletra(palavra, chute)))
       letras_restantes = letras_restantes - len(posicaoletra(palavra, chute))
    if(letras_restantes != 0):
        print("te restam {} tentativas de erro\n".format(tentativas))
    else:
        print("parabéns você ganhou o jogo!")
        break
    if (tentativas == 0):
        print("você perdeu o jogo")
        break






