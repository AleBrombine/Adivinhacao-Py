import random

def jogar():

    print("************************************")
    print("* Bem vindo ao jogo de Adivinhação *")
    print("************************************")


    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3
    pontos = 1000

    print ("Escolha a dificuldade:")
    print ("(1) Fácil (2) Médio (3) Difícil")

    dificuldade = int(input ("Selecione a dificuldade: "))

    
   # dificuldade0 = input("Selecione a dificuldade: ")
    #while not dificuldade0.isdigit:
          #  dificuldade0 = input("Selecione a dificuldade: ")
    #dificuldade = int(dificuldade0)


    if(dificuldade == 1):
        total_de_tentativas = 20
    elif (dificuldade == 2):
        total_de_tentativas = 10
    else: 
        total_de_tentativas = 5    
        

    rodada = 1

    for rodada in range ( rodada, total_de_tentativas + 1):
        print("tentativa {} de {}" .format (rodada, total_de_tentativas))

        chute__str = input("Coloque um número entre 1 e 100:", )
        print("Você digitou:", chute__str)
        chute= int(chute__str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue
        
        

        acertou = (chute == numero_secreto)
        maior   = (chute > numero_secreto)
        menor   = (chute < numero_secreto)


        if(acertou):
            print("Você acertou e fez {} pontos!" .format(pontos))
            break
        else: 
            if(maior):
                print("Você errou! Seu chute foi maior que o numero secreto")
            elif (menor):
                print("Você errou! Seu chute foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute) 
            pontos = pontos - pontos_perdidos
                

    print("O Jogo acabou")

if(__name__== "__main__"):
    jogar()
