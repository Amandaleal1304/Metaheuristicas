import math
import random
def bin2float (bits, a, b):
    # calulando o valor inteiro 
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

s = gera_solucao(30)
print(avalia_solucao(s))