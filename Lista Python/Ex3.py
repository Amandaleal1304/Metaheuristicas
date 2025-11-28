alunos = []

print("Digite o nome e nota de 10 alunos: ")

for i in range(10):
    print(f"\nAluno {i+1}:")
    nome = input("Nome: ")
    nota = float(input("Nota (0 a 10): "))
    
    aluno_dicionario = {
        "nome": nome,
        "nota": nota
    }
    alunos.append(aluno_dicionario)

print("\nAlunos Aprovados (Nota >= 6)")

for aluno in alunos:
    if aluno["nota"] >= 6:
        print(f"Nome: {aluno['nome']}, Nota: {aluno['nota']}")