'''
Crie uma lista de dicionários (de 4 ou mais elementos), em que cada elemento possui o nome e a nota dos alunos e ordene a lista de maneira decrescente por nota.
OBS: Faça o exercício utilizando apenas estruturas básicas, sem chamar funções de sort ou algo do tipo.
'''

students = [
    {'nome': 'Bruno', 'nota': 7 },
    {'nome': 'Carem', 'nota': 9 },
    {'nome': 'Lucas', 'nota': 8 },
    {'nome': 'Eduardo', 'nota': 6},
    {'nome': 'Edson', 'nota': 3}
]



def ordenar_notas(lista):
    order = True
    while order:
        order = False
        for i in range(len(lista) - 1):
            if lista[i]['nota'] < lista[i + 1]['nota']:
                lista[i] = lista[i + 1]
                lista[i + 1] = lista[i]
                order = True

    for student in lista:
        print(f'Aluno {student['nome']} - Nota: {student['nota']}')

ordenar_notas(students)

