saldo = 100
limite = 200

if saldo >= 0:
    print(f"Seu saldo atual é R$ {saldo:.2f}")
elif limite > 0:
    print(f"Seu limitee atual é R$ {limite:.2f}")
else:
    print(f"Seu saldo atual sem limite é: R$ {saldo:.2f}")
    print(f"Seu limite atual é: R$ {limite:.2f}")
