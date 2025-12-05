import math
import random
def bin2float (bits, a, b):
    g = 0
    n = len(bits)#tamanho do vetor ou seja quantidade de bits [0, 1, 0, 1]
    for i in range (n):
        #formula para calcular o valor inteiro
        #pega o valor de cada posicao do vetor e multiplica pelo expoente 2 ^n -i-1
        g += bits[i] * 2 ** (n - i - 1) # n - i - 1 por que a formula começa em 0 e nao em 1
    #calculo do valor real
    return  a + (g / (2**n - 1)) * (b - a)

def f(x, y): 
    return(5 + math.sin(x) * math.sin(y) + 0.5
           * math.sin(2*x) * math.sin(2*y)
           - 0.1 * (x**2 + y**2)
           )
 
def gera_solucao(n): #primeira solução n = tamanho do array
    s = []
    for i in range(n):
        s.append(random.randint(0, 1))#variavel entre 0 e 1 aleatoria
    return s


def avalia_solucao(sol): # avalia a qualidade da solução
    min_x, max_x = -8, 8 #minimo e maximo de x e y
    min_y, max_y = -8, 8
    n = len(sol)#tamanho do vetor
    m = n//2 #metado do vetor (// = divisao inteira)
    sol_x = sol[:m]#do inicio a metade 
    sol_y = sol[m:] #metade para frente
    x = bin2float(sol_x, min_x, max_x)#bin2float converte o binario para float
    y = bin2float(sol_y, min_y, max_y)
    return f(x, y)

def hill_climbing(bits, max_it):#bits = tamanho do array, max_it = numero de iteracoes
    sol_atual = gera_solucao(bits) #gera uma solucao aleatoria
    fitness_atual = avalia_solucao(sol_atual)#avalia a solucao
    for _ in range(max_it):
        sol_vizinha = sol_atual.copy()#cria uma copia da solucao atual
        r = random.randint(0, bits - 1) #gera um numero aleatorio entre 0 e o tamanho do array
        sol_vizinha[r] = 1 - sol_vizinha[r] #acha uma posicao e inverte o bit [0 -1 = 1 e 1 - 1 = 0]
        fitness_vizinha = avalia_solucao(sol_vizinha) #avalia a solucao vizinha
        if fitness_vizinha > fitness_atual: #se a solucao vizinha for melhor que a atual
            sol_atual = sol_vizinha #atualiza a solucao atual
            fitness_atual = fitness_vizinha #atualiza o fitness atual

    return sol_atual, fitness_atual

#   MAIN    
sa, fa = hill_climbing(30, 1000)        
print(sa)
print(fa)
        
