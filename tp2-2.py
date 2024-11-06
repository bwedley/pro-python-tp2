'''
Crie duas tuplas e verifique se elas possuem os mesmos elementos,
independente da ordem (Ex: tupla1 = (1,3,5) e tupla2 = (5, 1, 3) possuem SIM os mesmos elementos).
'''

tupla1 = (1, 3, 5)
tupla2 = (5, 1, 3)
tupla3 = (4, 2, 1, 3, 6, 0, 9, 9)
tupla4 = (0, 9, 6, 3, 1, 4, 9, 2)

def comp_tupla(a, b):
    if set(a) == set(b):
        print('possuem os mesmos elementos')
    else:
        print('não possuem os mesmos elementos')

comp_tupla(tupla1, tupla2) #mesmos valores
comp_tupla(tupla3, tupla4) #mesmos valores
comp_tupla(tupla1, tupla3) #valores diferentes
comp_tupla(tupla2, tupla4) #valores diferentes