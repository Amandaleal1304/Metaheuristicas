import random
def gera_solucao(n):
    s = []
    i = 0 
    while i < n:
        s.append(random.randint(0, 1))#variavel entre 0 e 1 aleatoria
        i += 1
    return s

def avalia_solucao(solucao): #conta quantos 1 tem e retorna a soma
    return sum(solucao)

def heuristica_aleatoria(n, iteracoes):#n (tamanho)
    melhor_solucao = None #variavel vazia
    melhor_avaliacao = -1
    i = 0
    while i < iteracoes:
        solucao = gera_solucao(n) #gera uma solucao aleatoria
        avaliacao = avalia_solucao(solucao) #avalia a solucao
        if avaliacao > melhor_avaliacao: #se a avaliacao for maior que a melhor avaliacao 
            melhor_solucao = solucao
            melhor_avaliacao = avaliacao
        i += 1
    return melhor_solucao, melhor_avaliacao
      



s, a = heuristica_aleatoria(10, 10000) #variavel recebe o resultado da funcao 
print(s)# imprime a solucao
print(a)# imprime o valor da funcao


# #começa a main
# a = gera_solucao(5) #variavel recebe o resultado da funcao
# print(a)
# print(avalia_solucao(a))#imprime o valor da funcao
