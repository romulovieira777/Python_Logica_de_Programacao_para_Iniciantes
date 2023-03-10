"""
Coleta de dados valor sempre positivo.

Quantidade de vendas - contador.

Valor médio das vendas.

Valor total das vendas.

Enquanto o número - 1.
"""

dadoVenda = 0
contador = 0
valorMedioDasVendas = 0
valorTotalDasVendas = 0

while dadoVenda >= 0:
    dadoVenda = int(input("Digite o valor da venda, ou - 1 para finalizar.\n: "))
    if dadoVenda >= 0:
        contador = contador + 1
        valorTotalDasVendas = valorTotalDasVendas + dadoVenda

valorMedioDasVendas = valorTotalDasVendas / contador

print(f"Valor total das vendas: {valorTotalDasVendas}")
print(f"Valor médio das vendas: {valorMedioDasVendas}")
print(f"Quantidade de vendas: {contador}")
