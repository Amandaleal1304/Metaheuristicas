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


#                       MAIN
b = [1, 0, 1, 1, 0]
print(bin2float(b, 0, 10))#intervalo de 0 a 10
           
