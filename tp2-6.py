'''
Crie uma lista (maior que 5 elementos) e encontre os dois números cuja soma seja o mais próximo possível de zero.
'''

numeros = [-2, -10, 9, 13, -1, 5, 7]
numeros2 = [-139, -123, 231, 223, -766, 872, -321]

def achar_mais_proximo(lista):
    first_num = lista[0]
    second_num = lista[1] 
    mais_proximo_zero = first_num + second_num
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            soma = lista[i] + lista[j]
            if (abs(soma) < abs(mais_proximo_zero)):
                mais_proximo_zero = soma
                first_num = lista[i]
                second_num = lista[j]
    print(f'Os dois números somados mais próximo de zero são: {first_num} e {second_num}, que somam {mais_proximo_zero}')

achar_mais_proximo(numeros)
achar_mais_proximo(numeros2)
