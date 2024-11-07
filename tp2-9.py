''' 
Crie um programa que verifica se uma palavra fornecida pelo usuário é um palíndromo.
OBS: Non-case sensitive e sem contar os espaços (Ex: "A mala nada na lama" é um palíndromo).
'''
def verify_pali():
    frase = input("Digite uma palavra ou frase: ")

    frase_sem_espaços = frase.replace(" ", "").lower()

    if frase_sem_espaços == frase_sem_espaços[::-1]:
        print("A entrada é um palíndromo.")
    else:
        print("A entrada não é um palíndromo.")

verify_pali()


#Código reaproveitado do tp1-13