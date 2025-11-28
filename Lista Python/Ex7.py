frutas_cadastradas = set()
contador_repetidas = 0

while True:
    nome = input("Digite o nome de uma fruta (ou 'sair' para parar): ")
    
    if nome == 'sair':
        break
    
    if nome in frutas_cadastradas:
        contador_repetidas += 1
    else:
        frutas_cadastradas.add(nome)

print("\n--- Frutas Cadastradas ---")
for fruta in frutas_cadastradas:
    print(fruta)

print("\nTotal de frutas não cadastradas (repetidas):", contador_repetidas)