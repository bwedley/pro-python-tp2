'''Número Mágico: Crie um código para adivinhar um número aleatório entre 1 e 20 com um limite de 4 tentativas
(ou seja, o programa recebe essas tentativas do usuário e verifica se o número que o usuário escreveu é o número mágico)
 OBS: Para cada número digitado, informe se ele está abaixo ou acima do número mágico.
'''
import random

def secret_number():
    curr_try = 0
    tries = 4
    secret_number = random.randint(1, 20)

    print("Tente adivinhar o número secreto entre 1 e 20.")

    while curr_try < tries:
        palpite = int(input("Digite seu palpite: "))
    
        if palpite == secret_number:
            print("Parabéns! Você acertou o número secreto!")
            break
        elif palpite < secret_number and curr_try < 3:
            print(f"Muito baixo! Tente novamente. Você tem {(tries - curr_try) - 1} tentativas restantes")
            curr_try+=1
        elif palpite > secret_number and curr_try < 3:
            print(f"Muito alto! Tente novamente. Você tem {(tries - curr_try) - 1} tentativas restantes")
            curr_try+=1
        elif curr_try == 3:
            print(f"Você não acertou, o jogo chegou ao fim e o número era {secret_number}")
            break

secret_number()

#Código reutilizado to tp1-6 com adaptações para satisfazer o exercício atual