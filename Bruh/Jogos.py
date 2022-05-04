import adivinha
import forca

def escolher_jogos():
    print("Escolha o jogo:")
    print("1- Jogo do Adivinha // 2- Jogo da Forca\n")
    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogo do Adivinha\n")
        adivinha.jogar()
    elif(jogo == 2):
        print("Jogo da Forca\n")
        forca.jogar()
if(__name__ == "__main__"):
    escolher_jogos()
