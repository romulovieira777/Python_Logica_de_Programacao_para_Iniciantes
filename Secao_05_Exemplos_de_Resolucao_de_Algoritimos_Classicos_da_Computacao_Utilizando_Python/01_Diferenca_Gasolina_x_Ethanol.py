"""
Escrever um algoritimo que receba o valor com o preço da gasolina e do ethanol.

Calcule a diferença de valores entre o ethanol e gasolina.

Se o resultado for inferior a 0,7, o derivado da cana-de-açúcar é o melhor para abastecer.

Se o resultado for maior que 0,7, então a gasolina é a melhor.
"""
precoGasolina = float(input("Digite o valor da gasolina: "))
precoEthanol = float(input("Digite o valor do etanol: "))

diferenca = 0.00

if precoGasolina > 0:
    diferenca = precoEthanol / precoGasolina
    print(f"A diferença entre Ethanol x Gasolina é: {diferenca:.2f}")

    if diferenca < 0.7:
        print("O melhor combustível é o Etanol")
    else:
        print("O melhor combustível é a Gasolina")
else:
    print("Informe todos os dados.")
