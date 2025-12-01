import random

N = 20 
OTIMO_GLOBAL = N #valor máximo de 1s.

def avalia_solucao(solucao): 
    return sum(solucao) #soma os 1s

def gera_solucao(tamanho):#primeira solução
    return [random.randint(0, 1) for _ in range(tamanho)] #cria um array binário (0 ou 1) aleatório.

def gera_vizinhanca(solucao_atual): # vai gerar todas as soluções vizinhas a inicial
    vizinhanca = []
    
    for i in range(len(solucao_atual)): # faz iterações em cada bit do array
        solucao_vizinha = list(solucao_atual) #cria uma cópia da solução atual.
        solucao_vizinha[i] = 1 - solucao_vizinha[i] # Inverte o bit atual
        vizinhanca.append(solucao_vizinha) # Adiciona a nova versão (o vizinho) à lista.
        
    return vizinhanca

def busca_local_onemax():
    solucao_atual = gera_solucao(N) #gera o ponto de partida aleatório.
    melhor_avaliacao = avalia_solucao(solucao_atual) #avalia a qualidade inicial (quantos 1s).
    melhor_solucao = solucao_atual[:] #guarda a melhor solução encontrada até agora.
    
    print(f"Configuração Inicial: {melhor_solucao}")
    print(f"Avaliação Inicial: {melhor_avaliacao}\n")
    
    iteracao = 0
    while melhor_avaliacao < OTIMO_GLOBAL: #enquanto o ótimo global não for atingido.
        iteracao += 1
        
        vizinhanca = gera_vizinhanca(solucao_atual) # Gera todas as soluções vizinhas (o entorno).
        
        melhor_vizinho = None
        avaliacao_melhor_vizinho = -1 # variavel vazia para guardar a melhor avaliação de um vizinho.

        for vizinho in vizinhanca: 
            avaliacao_vizinho = avalia_solucao(vizinho) #avalia a qualidade do vizinho.
            
            if avaliacao_vizinho > avaliacao_melhor_vizinho: #procura o melhor vizinho.
                avaliacao_melhor_vizinho = avaliacao_vizinho
                melhor_vizinho = vizinho

        if avaliacao_melhor_vizinho > melhor_avaliacao:
            melhor_solucao = melhor_vizinho[:] #atualiza a melhor solução encontrada.
            melhor_avaliacao = avaliacao_melhor_vizinho
            solucao_atual = melhor_vizinho[:]
            
            print(f"Iteração {iteracao}: Nova avaliação encontrada: {melhor_avaliacao}")
            
        else:
            print(f"\nBusca parou na Iteração {iteracao}: Nenhuma melhoria encontrada no entorno.") 
            break

    print("\n--- Resultado Final ---")
    print(f"Melhor configuração encontrada: {melhor_solucao}")
    print(f"Valor avaliado (Avaliação): {melhor_avaliacao}")
    print(f"Total de Iterações: {iteracao}")
#---------------------------- MAIN ---------------------------------
busca_local_onemax() # Inicia o algoritmo.