'''
Joel possui uma barraca na feira e quer dar um presente a um cliente. Crie um programa que receba do usuário uma lista de frutas disponíveis na barraca e
as quantidades correspondentes de cada fruta. O programa deve escolher aleatoriamente uma fruta para presentear o cliente. Se o número de quantidades
fornecido for maior do que o número de frutas, o programa deve contabilizar apenas até o último índice da lista de frutas. Caso o número de quantidades seja
menor do que o número de frutas, o programa deve solicitar ao usuário que reescreva a lista de quantidades (Ex: input do usuário: ‘maçã, banana, laranja’ | ‘10, 5, 8’).
'''
import random

def lista_de_frutas():
    frutas = input("Digite as frutas disponíveis no momento: ").split(",")
    lista_frutas = [fruta.strip() for fruta in frutas]
    return lista_frutas

def quantidade_frutas(qtde_frutas):
    while True:
        try:
            qtde_digitada = list(map(int, input("Digite a quantidade de cada fruta: ").split(",")))
            if len(qtde_digitada) > qtde_frutas:
                qtde_digitada = qtde_digitada[:qtde_frutas]
            elif len(qtde_digitada) < qtde_frutas:
                print("Erro: as quantidades não correspodem.\nPor favor, reveja as quantidades" )
                continue
            return qtde_digitada
        except:
            print(f"Erro {qtde_digitada}")

def sortear_presente(frutas, qtde):
    fruta_sorteada = random.choice(frutas)
    print(f"Parabéns, você ganhou a fruta {fruta_sorteada}!")

def realizar_sorteio():
    frutas = lista_de_frutas()
    quantidade = quantidade_frutas(len(frutas))
    sortear_presente(frutas, quantidade)

realizar_sorteio()
