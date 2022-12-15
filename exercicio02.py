# Escrever um programa que gera e escreve o somatório dos numeros impares entre 100 e 200

# Escrever um programa que realiza a leitura de dez numeros e exiba a media dos numeros pares

# Escrever um programa que realiza a leitura de um numero e no final. exiba o resultado da tabuada conforme o exemplo
# abaixo: O Usuario informou o ñumero 7. 7x1 = 7 7x2=14 ... 7x10=70

# exercicio01

soma = 0
for numero in range(100, 200):
    if numero % 2 != 0:
        print(numero)
        soma = soma +numero
print(soma)

# exercicio02

somaPares = 0
quantidade = 0
for i in range(10):
    numero = int(input("Digite o numero: "))
    if numero % 2 == 0:
        somaPares = somaPares + numero
        quantidade = quantidade + 1
media = somaPares/quantidade
print(media)


# exercicio03
numero = int(input("Digite um numero: "))
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")
