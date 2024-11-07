'''
Crie um programa que permita ao usuário registrar as notas de uma turma de estudantes.
O usuário deve inserir os nomes dos alunos e suas respectivas notas. O programa deve continuar solicitando entradas até que o usuário digite "fim".
Após o término, o programa deve exibir os nomes dos alunos junto com suas notas.
'''
MIN_LEN_NAME = 3
FLAG = 'fim'

def enter_name():
    while (True):
        name = input("Digite o nome do aluno: ")
        if(len(name) < MIN_LEN_NAME):
            print("Erro")
        else:
            break
    return name

def enter_score():
    while (True):
        try:
            score = float(input("Digite a nota do aluno: "))
            break
        except:
            print("Erro")
    return score

def enter_student():
    classes = []
    name = enter_name()
    while(name.lower() != FLAG):
        score = enter_score()
        student = [name, score]
        classes.append(student)
        name = enter_name()
    return classes

def exibir(classes):
    for student, score in classes:
        print(f'Aluno: {student}, Nota: {score}')

classes = enter_student()

exibir(classes)



