'''
Crie dois dicionários (com 2 ou mais elementos) e verifique se um é subconjunto de outro.
'''

dict1 = {'Bruno': 1993, 'Carem': 1998}
dict2 = {'Lucas': 1994, 'Bruno': 1993, 'Laura': 1996, 'Carem': 1998}
dict3 = {'Jean': 1994, 'Felipe': 1993, 'Carem': 1998}
dict4 = {'Bruno': 1993, 'Carem': 1998, 'Lucas': 1994}

def verify_is_sub(dictMenor, dictMaior):
    return all(item in dictMaior.items() for item in dictMenor.items())

def is_sub(func):
    if func:
        print('É subconjunto')
    else:
        print('Não é subconjunto')

# verify_is_sub(dict1, dict2)
is_sub(verify_is_sub(dict1, dict2)) #True
is_sub(verify_is_sub(dict2, dict3)) #False
