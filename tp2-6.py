'''
Crie uma lista (maior que 5 elementos) e encontre os dois números cuja soma seja o mais próximo possível de zero.
'''

numeros = [-5, -10, 9, 13, -1, 5, 7]

first_num = numeros[0]
second_num = numeros[1]

minor = first_num + second_num

for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        soma = numeros[i] + numeros[j]
        if (soma > 0 and (minor <= 0 or soma < minor)) or (soma < 0 and (minor > 0 or soma > minor)):
            minor = soma
            first_num = numeros[i]
            second_num = numeros[j]
print(f'Os dois números somados mais próximo de zero são: {first_num} e {second_num}, que somam {minor}')

#OBS: ainda não concluido, condicional não satisfaz o exercício