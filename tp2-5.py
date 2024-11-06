'''
Crie um dicionário que mapeia alunos e suas notas e retorne um novo dicionário que classifique os alunos em "Aprovado" (nota >= 7) e
"Reprovado" caso contrário (Ex: notas = {'Ana': 8.5, 'Pedro': 6.0, 'Maria': 7.5, 'José': 5.5} deve retornar {'Aprovado': ['Ana', 'Maria'], 'Reprovado': ['Pedro', 'José']}).
'''
notas = {'Ana': 8.5, 'Pedro': 6.0, 'Maria': 7.5, 'José': 5.5}
notas2 = {'Bruno': 9.5, 'Lucas': 9, 'Ana': 4.5, 'Roberto': 3, 'Angelo': 5, 'Rogério': 7, 'Carem': 8.5}

def verify_result(dictNota):
    final_result = {'Aprovado':[], 'Reprovado': []}
    for aluno, nota in dictNota.items():
        if nota >= 7:
         final_result['Aprovado'].append(aluno)
        else:
            final_result['Reprovado'].append(aluno)
    print(final_result)

verify_result(notas)
verify_result(notas2)


