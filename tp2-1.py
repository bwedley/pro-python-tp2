'''
Crie um dicionário com as idades de várias pessoas e retorne um novo dicionário que contenha apenas as pessoas maiores 
de idade (Ex: idades = {'Alice': 22, 'Bob': 17, 'Carol': 19, 'David': 16} deve retornar {'Alice': 22, 'Carol': 19})
'''

people_dict = {'Alice': 22, 'Bob': 17, 'Carol': 19, 'David': 16}
people_dict2 = {'André': 15, 'Carem': 28, 'Lucas': 30, 'Breno': 16, 'Edson': 31}

def legal_age(dicti):
   print(dict(filter(lambda person: person[1] >= 18, dicti.items())))

legal_age(people_dict) #Alice, Carol
legal_age(people_dict2) #Carem, Lucas, Edson
