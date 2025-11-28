pessoas = () #tupla

for i in range (5):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    pessoas += ((nome, idade),) #tupla dentro de tupla

print("\n--- Todos os Dados Cadastrados ---")
for n, i in pessoas:
        print(f"Nome: {n}, Idade: {i} anos")

print("\n--- Pessoas Maiores de Idade (>= 18 anos) ---")

for nome_pessoa, idade_pessoa in pessoas:
    if idade_pessoa >= 18:
        print(nome_pessoa)

