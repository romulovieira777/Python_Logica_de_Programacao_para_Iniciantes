"""
Escreva um programa em Python que receba dois números inteiros.

E calcula a diferença entre os dois e em seguida apresente o seu sucessor e antecessor.
"""
# Solution I
valorA = int(input("Digite o valor de A: "))
valorB = int(input("Digite o valor de B: "))

diferenca = 0

if valorA > 0 and valorB > 0:
    diferenca = valorA - valorB
    print(f"A diferença entre A e B é: {diferenca}")
    print(f"O sucessor de A é: {valorA + 1}")
    print(f"O antecessor de B é: {valorB - 1}")
else:
    print("Informe todos os dados.")


# Solution II

# Declaração de variáveis
diferenca = 0
sucessor = 0
antecessor = 0
valorA = 0
valorB = 0


# Entrada de dados
valorA = int(input("Digite o valor de A: "))
valorB = int(input("Digite o valor de B: "))

diferenca = valorA - valorB
sucessor = diferenca + 1
antecessor = diferenca - 1

print(f"Valor A, Valor B: {valorA}, {valorB}")
print(f"Diferença: {diferenca}")
print(f"Sucessor, Antecessor: {sucessor}, {antecessor}")

