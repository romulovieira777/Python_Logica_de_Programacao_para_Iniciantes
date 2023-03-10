# saldo é R$ 100,00
# pode sacar qualquer valor até R$ 100,00
# sacar R$ 80,00 - ok saldo restante R$ 20,00
# sacar R$ 10,00 - ok saldo restante R$ 90,00
# sacar 25,00 - negado sem saldo
# IF ELSE

saldo = 100

if saldo >= 0:
    print(f"Seu saldo atual é R$ {saldo:.2f}")
else:
    print(f"Seu saldo atual é (negativo) R$ {saldo:.2f}")

valorSaque = 80

if saldo - valorSaque >= 0:
    print(f"Saque efetuado - R$ {valorSaque:.2f}")
    saldo = saldo - valorSaque
    print(f"Seu saldo atual é R$ {saldo:.2f}")
else:
    print(f"Saque não efetuado no valor de R$ {valorSaque:.2f}")

valorSaque = 10

if saldo - valorSaque >= 0:
    print(f"Saque efetuado - R$ {valorSaque:.2f}")
    saldo = saldo - valorSaque
    print(f"Seu saldo atual é R$ {saldo:.2f}")
else:
    print(f"Saque não efetuado no valor de R$ {valorSaque:.2f}")

valorSaque = 25

if saldo - valorSaque >= 0:
    print(f"Saque efetuado - R$ {valorSaque:.2f}")
    saldo = saldo - valorSaque
    print(f"Seu saldo atual é R$ {saldo:.2f}")
else:
    print(f"Saque não efetuado no valor de R$ {valorSaque:.2f}")
    print(f"Seu saldo atual é R$ {saldo:.2f}")
