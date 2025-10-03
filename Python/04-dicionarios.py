aluno = {
    "nome":"Ana",
    "idade" : 20,
    "curso" : "BSI"
}


print(aluno["nome"])
print(aluno["idade"])
print(aluno["curso"])

#alterar valores
aluno["idade"] = 21 #altera o valor da chave idade
print(aluno) 

#adicionar valores
aluno["matricula"] = 20251010 #não existe então sera adicionada ao dicionario
print(aluno)

#remover valores
del aluno["curso"]#remove o atributo curso
print(aluno)

#retornar e remover
mat = aluno.pop("matricula")#retorna e retira o valor do atributo matricula
print(mat) #retorna 20251010
print(aluno) #retorna o dicionario sem o atributo matricula

#verificar se um atributo existe
if "idade" in aluno:
    print('SIM')
else:
    print('NÃO')

#retornar os atributos
print(aluno.keys()) #retorna os atributos do dicionario

 #Lista(vetor) que dentro tem um dicionario (lista de struct) e disc é uma lista(vetor)
alunos = [
    {"nome": "Ana", "matricula": "20251010", "disc":["Alg", "Mth", "BD"]}
]
alunos.append({"nome":"Carlos", "matricula": "20242020", "disc":["Alg", "Mth", "BD"]})
print(alunos)

ponto = {"x":10, "y":20}
print(ponto.values()) #retorna os valores do dicionario [10,20]
print(ponto.items()) #retorna os pares chave/valor [(x,10),(y,20)]



