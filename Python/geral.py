# nome = imput ("Informe seu nome: ")
# pedindo informações ao usuario do tipo inteiro 
# x = int (input("Informe um numero inteiro: "))
# y = int (input("Informe outro numero inteiro: "))
# z = x + y
# print("A soma é ", z)

# a = float(input("Informe um numero real: "))
# a /= 2
# print (f" O resultado da divisao e {a}")

# idade = int (input("Informe sua idade: "))

# if idade >= 18:
#     print("Maior de idade")
# else:
#     print("Menor de idade")
#     print("Aproveite sua juventude")

# if idade < 12:
#     print('Criança')
# elif idade < 18:#elif é se não se 
#     print('Adolescente')
# else:
#     print('Adulto')
#     print('Aproveite sua vida')

#modo resumido mas nao muito indicado 
# print("Maior de idade" if idade >= 18 else "Menor de idade")

############################ switch case do python
# match idade:
#     case 1:
#         print("Bebe")
#     case 7:
#         print("Criança")
#     case 18:
#         print("Adulto")
#     case _:
#             print("Idade nao reconhecida")

############################### Repetições
# i = 0
# while i < 10:
#     print('Amanda')
#     i += 1


################################## Fatorial
# numero = int(input("Digite um número inteiro : "))

# n = numero
# fatorial = 1
# while n > 1:
#     fatorial = fatorial * n
#     n = n - 1 

# print(f"O fatorial de {numero} é {fatorial}.")


numero = int(input("Digite um número inteiro: "))
fatorial = 1
for i in range(1, numero + 1):
    fatorial = fatorial * i

print(f"O fatorial de {numero} é {fatorial}.")

