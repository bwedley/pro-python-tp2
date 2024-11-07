'''
Defina uma função chamada ‘dividir’ que recebe dois números e retorna dois outputs: o resultado inteiro da divisão e o resto.
Escreva uma docstring para documentar o que a função faz, quais são seus parâmetros, e o que ela retorna.
'''

def dividir(a, b):
    '''
    Esta função realiza a divisão de dois números e retorna dois resultados: sendo o primeiro a divisão inteira e o segundo o resto da divisão
    A função conta com um tratamento de exceção para o caso de parâmetros com tipos diferentes de int/float ou uma eventual tentativa de divisão por 0.

    Parâmetros:
    a(int, float): dividendo.
    b(int, float): divisor.

    Retorno:
    f-string com parâmetros e resultados das divisões:
    Resultado da divisão inteira (a // b)
    Resultado do resto da divisão (a % b)
    '''
    try:
        inteiro = a // b
        resto = a % b
        print(f'Para {a}/{b} Teremos:\nResultado inteiro: {inteiro}\nResto da divisão: {resto}')
    except:
        print(f'Erro, impossível dividir {a} por {b}')

dividir(5, 2.5)
