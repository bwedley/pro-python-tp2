'''
Defina uma função que receba um nome e uma idade como argumentos obrigatórios e uma cidade como argumento opcional (valor padrão "Desconhecida").
A função deve imprimir uma mensagem personalizada com essas informações. Ex: "Maria tem 30 anos e mora em São Paulo".
'''

def name_age_city(name, age, city="Desconhecida"):
    if(city == "Desconhecida"):
        print(f'{name} tem {age} anos e mora em uma cidade {city}')
    else:
        print(f'{name} tem {age} anos e mora em {city}')

name_age_city('Maria', 30)