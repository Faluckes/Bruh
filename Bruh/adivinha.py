from random import randint

def jogar():
    print("===================================================")
    print("Jogo do Adivinha. Acerte e ganhe tiro no pé")
    print("===================================================")
    print("TOTALMENTE RANDOMIZADO!!")
    print("===================================================\n")

    numero_aleatorio = randint(1, 50)
    tentativas = 0
    rodada = 1
    pontos = 1000



    print("Qual Nível de Dificuldade?")
    print("1- Fácil // 2- Normal // 3- Difícil // 4- IMPOSSÍVEL")

    nivel = int(input("Defina o Nível de Dificuldade: "))

    if(nivel == 1):
        tentativas = 20
        print("Você escolheu a Dificuldade Fácil!")
    elif(nivel == 2):
        tentativas = 15
        print("Você escolheu a Dificuldade Normal!")
    elif(nivel == 3):
        tentativas = 10
        print("Você escolheu a Dificuldade Difícil!")
    elif(nivel == 4):
        tentativas = 5
        print("Você escolheu a Dificuldade IMPOSSÍVEL!")
        
    for rodada in range (1, tentativas + 1):
        print("\nVocê tem {} tentativas para acertar o número de 1 a 50".format(tentativas))
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute_str = input("Digite o número: ")
        chute = int(chute_str)
        print("Você colocou o número: ", chute_str)
        if(numero_aleatorio == chute):    
            print("\n===================================================")
            print("Você acertou o número, parabéns!")
            print("=================================================== \n")

            break;

        else:
            if(chute > numero_aleatorio):
                print("\n===================================================")
                print("Você errou! O chute foi maior que o Numero randomizado")
                print("=================================================== \n")
                pontos_perdidos = chute - numero_aleatorio
                pontos = pontos - pontos_perdidos

            elif(chute < numero_aleatorio):
                print("\n===================================================")
                print("Você errou! O chute foi menor que o Numero randomizado")
                print("=================================================== \n")
                pontos_perdidos = numero_aleatorio - chute
                pontos = pontos - pontos_perdidos

    print("Você fez {} Pontos :D".format(pontos))
    print("O numero randomizado era: ", numero_aleatorio)
    print("Acabou \n \n")
    print("Aperte ENTER para finalizar a tarefa")
    input()

if(__name__ == "__main__"):
    jogar()



