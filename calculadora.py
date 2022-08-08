"""
Aluno: Bruno Yudi Mino Okada

Você deverá desenvolver um programa, na sua linguagem de programação favorita, que leia
uma string de entrada e execute a operação matemática contida nesta string. Esta string irá
representar operações matemáticas segundo uma variação da RPN, que inclui obrigatoriamente
parênteses para limitar as operações, conforme exemplos a seguir:
a) (2 3 +) = 5
b) (3 4 *) = 12
c) (4 2 2 /) = 1
d) ((4 2 +) 3 *) = 18
O seu programa deverá ser capaz de realizar as seguintes operações:
• Adição representada por +;
• Subtração representada por -;
• Multiplicação representada por *;
• Divisão representada por /;
As operações devem ser realizadas com número reais, mesmo que todos os exemplos aquiutilizados sejam com números inteiros.
As operações podem ser aninhadas, sem qualquer limite,como pode ser visto nos exemplos a seguir:
• ((3 4 +) (4 2 /) *) = 14
• ((3 4 +) (4 (1 1 +) /) *) = 14
Os operandos serão separados de outros operandos e dos operadores por um caractere deespaço.
Por fim, O sinal de igual e todos os resultados que estão a direita deste símbolo neste enunciado não fazem
parte da string que deverá ser lida e estão aqui apenas para facilitar o entendimento.
O teste será realizado diretamente no ambiente do repl.it, com a digitação de um conjunto de expressões pelo professor.
"""


def calculadora():
    # Pega a entrada do código
    equacao = input("Qual a equação a ser resolvida? ")

    equacao = equacao.replace('(', ' ')
    equacao = equacao.replace(')', ' ')
    # Transforma a equação em lista
    equacao = equacao.split()
    # pilha para adicionar os elementos e resolver a equação
    lista_de_elementos = []

    for elemento in equacao:
        # Verifica se cada elemento da String de entrada é um número ou operador
        if elemento not in '+-*/':
            # Se for um número, é adicionado na pilha como um número real
            lista_de_elementos.append(float(elemento))
        else:
            # Caso seja um operador, pega os ultimos dois numeros da pilha, realiza a operação indicada pelo operador
            # e adiciona o resultado novamente à pilha
            segundo_numero = lista_de_elementos.pop()
            primeiro_numero = lista_de_elementos.pop()

            if elemento == '*':
                lista_de_elementos.append(primeiro_numero * segundo_numero)
            elif elemento == '/':
                lista_de_elementos.append(primeiro_numero / segundo_numero)
            elif elemento == '+':
                lista_de_elementos.append(primeiro_numero + segundo_numero)
            elif elemento == '-':
                lista_de_elementos.append(primeiro_numero - segundo_numero)

    # Quando não há mais elementos é obtido a resposta da entrada e mostrada ao usuário
    resposta = lista_de_elementos.pop()

    print("A resposta da equação inserida é: {}".format(resposta))


if (__name__ == "__main__"):
    calculadora()