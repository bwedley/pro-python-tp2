'''
Crie uma lista (de 4 ou mais elementos) e um programa que permita ao usuário acessar os elementos desta lista.
O usuário deve inserir um índice (número inteiro) para obter o elemento correspondente na lista.
Trate casos em que o índice inserido está fora do intervalo da lista ou se o usuário inserir algo que não seja um número
(Dica: ‘try’, ‘except’). Se ocorrer um erro, informe ao usuário qual o erro e permita que ele tente novamente.
'''

games_list = ['World of Warcraft', 'Valorant', 'Bloodborne', 'Elden Ring', 'Dark Souls', 'Death Stranding']

def get_element():
    while True:
        try:
            index = int(input(f"Digite um número inteiro até {len(games_list)} para acessar um elemento: "))
            print(games_list[index - 1])
            break
        except:
            print('Valor inválido, tente novamente')
get_element()