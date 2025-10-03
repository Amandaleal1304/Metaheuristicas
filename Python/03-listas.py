#criação de listas que não tem tipos definidos
frutas = ["maça", "banana", "uva"]

#mostra o vetor completo sem precisar de um for
print(frutas)

f1 = frutas[0] #mostra o primeiro elemento
f2 = frutas[1] #mostra o segundo elemento
f3 = frutas[2] #mostra o terceiro elemento

print(f1)
print(f2)
print(f3)

#Inserir elemetos na lista
frutas.append("melancia")#adiciona um elemento ao final da lista
print(frutas)#['maça', 'banana', 'uva', 'melancia']
frutas.insert(1, "pera")#adiciona um elemento em uma posicao especifica
print(frutas) #['maça', 'pera', 'banana', 'uva', 'melancia']

#Remover elementos da lista 
frutas.remove("uva")
print(frutas) #['maça', 'pera', 'banana', 'melancia']

del frutas[0]#remove o elemento na posição 0
print(frutas) #['pera', 'banana', 'melancia']

#Pegar elementos da lista
numeros = [10, 20, 30, 40, 50]
l2 = numeros[1:4] #pega os valores sem incluir o indice final (nao vai pegar o 40)
print(l2)

print(numeros[:3])#pega os valores ate o anterior ao 3 ou seja indice 2

print(numeros[-2:])#pega os valores anteriores ao 2 ou seja 40 e 50

#Concatenar listas
lista1 = [1, 2, 3]
lista2 = [4, 5]
lista_total = lista1 + lista2 #junta as listas
print(lista_total)

#Funcoes
idades = [15, 22, 30, 18]
print(len(idades))#mostra o tamanho da lista ou seja 3
print(max(idades))#mostra o maior elemento da lista ou seja maior idade que é 30
print(min(idades))#mostra o menor elemento da lista ou seja menor idade que é 15
print(sum(idades))#mostra a soma dos elementos da lista ou seja 75

t = 3 * idades
print(t) #vai triplicar a lista

if 20 in idades: #verifica se o elementoesta na lista
    print("SIM")
else: 
    print("NÃO")