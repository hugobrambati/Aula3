"""
Exemplo: Ler um numero e informar o mes correspondente
"""

mes = int(input("Informe o numero:"))

"""

No python não existe switch

"""


match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case other:
        print("Mês inválido")