cod = int(input("Digite o codigo do produto: "))

ids = [1001, 1324, 6548, 987, 7623]

if cod in ids:

    qnt = float(input(" Informe a quantidade desejada: "))

else:
    print("Codigo não encontrado!")
    quit()

match cod:
    case 1001:
        valor = qnt * 5.32
        print("O valor total da compra é: ", valor)

    case 1324:
        valor = qnt * 6.45
        print("O valor total da compra é: ", valor)

    case 6548:
        valor = qnt * 2.37
        print("O valor total da compra é: ", valor)

    case 987:
        valor = qnt * 5.32
        print("O valor total da compra é: ", valor)

    case 7623:
        valor = qnt * 6.45
        print("O valor total da compra é: ", valor)


