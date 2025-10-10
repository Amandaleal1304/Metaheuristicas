#os valores definidos nao podem ser mudados
coordenada = (10, 20)
print(coordenada)

#coordenada[0] = 30 #deu erro pois a tupla é imutavel 

print(coordenada[0])
print(coordenada[1])

cores = ("vermelho", "verde", "azul", "verde")#valores podem ser repetidos
t = len(cores)#retorna o tamanho da tupla
print(t)

t = cores.count("verde")#retorna quantas vezes o elemento aparece
print(t)

i = cores.index("vermelho")#retorna a posicao do elemento
print(i)

print(cores[1:3])#1 ate o anteriores ao 3
print(cores[:2])#dois primeiros
print(cores[:-2])#dois ultimos

ponto = (99, 200)
#desempacotamento
x, y = ponto
print(x)
print(y)

t = (10, 20, (30, 40)) #tupla dentro de tupla
print(t)#(10, 20, (30, 40))
print(t[2])#(30, 40)
print(t[2][0])#30
print(t[2][1])#40

t1 = (1, 2, 3)
t2 = (4, 5)
r = t1 + t2#uniao de tupla
print(r)

t3 = t1 * 3# triplica a tupla 
print(t3)#(1, 2, 3, 1, 2, 3, 1, 2, 3)

if "verde" in cores:
    print ("SIM")
else:
    print ("NAO")