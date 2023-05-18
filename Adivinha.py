import random

print("________________________________")
print("Bem vindo ao jogo de Advinhação!")
print("________________________________")

numero_secreto = (random.randrange(1,10))
total_de_tentativas = 0

print("Escolha o nível de dificuldade", numero_secreto)
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5



for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    sorteio_str = input("Digite o seu número entre 1 e 10: ")
    print("Voce digitou" , sorteio_str)
    sorteio = int(sorteio_str)

    if(sorteio < 1 or sorteio > 10):
        print("Você deve digitar um número 1 e 10!")
        continue

    acertou = numero_secreto == sorteio
    maior = sorteio > numero_secreto
    menor = sorteio < numero_secreto

    if (acertou):
        print("voce acertou")
        break

    else:
        if(maior):
          print("voce errou! O chute foi maior do que o número secreto.")
        if(menor):
          print("Voce errou! O seu chute é menor do que o número secreto.")


    print("Fim do jogo")



