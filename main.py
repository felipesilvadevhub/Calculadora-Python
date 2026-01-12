numero_1 = int(input("Digite o numero 1 > "))
numero_2 = int(input("Digite o numero 2 > "))

somar = input("Deseja somar? (sim ou nao) ").lower()

if somar == "sim":
    print("Somando...")
    print(numero_1 + numero_2)

elif somar == "nao":
    print("Operações disponíveis: +  -  *  /")
    quetipodeconta = input("Digite o tipo de conta > ")

    if quetipodeconta == "+":
        print(numero_1 + numero_2)

    elif quetipodeconta == "-":
        print(numero_1 - numero_2)

    elif quetipodeconta == "*":
        print(numero_1 * numero_2)

    elif quetipodeconta == "/":
        if numero_2 == 0:
            print("Erro: divisão por zero")
        else:
            print(numero_1 / numero_2)

    else:
        print("Operação inválida")
else:
    print("Resposta inválida")
