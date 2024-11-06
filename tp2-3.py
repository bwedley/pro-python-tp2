'''
Crie uma lista que possua números repetidos e conte a frequência de cada elemento
nessa utilizando um dicionário (Ex: lista = [4, 1, 5, 2, 3, 2, 4, 4] deve retornar dicionario = {1: 1, 2: 2, 3: 1, 4: 3, 5: 1}).
'''

list_numbers = [4, 1, 5, 2, 3, 2, 4, 4]
freq_numbers = {}

def count_elems(lista):
    for item in lista:
        if(item in freq_numbers):
            freq_numbers[item] += 1
        else:
            freq_numbers[item] = 1
    print(dict(sorted(freq_numbers.items())))

count_elems(list_numbers)