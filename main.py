import random
resposta = ['carro', 'passear', 'cachorro', 'mouse', 'celular', 'telefone', 'liquidificador', 'mexerica', 'cidade', 'cagar']
def gerar_palavra():
    global palavra
    palavra = random.choice(resposta)
    return palavra

def posicaoletra(string, char):
    pos = []
    for n in range(len(string)):
        if string[n] == char:
            pos.append(n+1)
    return pos

print("\n*********************************")
print("Bem vindo ao jogo da Forca!")
print("*********************************\n")
print("A Sua palavra contém" , len(gerar_palavra()) , "letras")

letras_restantes = len(palavra)
letras_chutadas = []
tentativas = 5
while tentativas > 0:

    chute = input("Digite o seu chute ")
    if (letras_chutadas.count(chute) > 0):
        print("você chutou uma letra repetida\n")
        continue
    else:
        letras_chutadas.append(chute)
    posicao = palavra.find(chute)
    if(posicao == -1):
        print("A palavra não contém essa letra\n")
        tentativas = tentativas - 1
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






