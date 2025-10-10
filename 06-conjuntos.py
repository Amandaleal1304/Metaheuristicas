#chave:valor é dicionario, valor entre viruglas é conjunto, {entre chaves}
numeros = {1, 2, 3, 4, 4, 5}
print(numeros)#existe relacao de ordem o 6 aparece no final e 4 nao repete

numeros.add(6)#adiciona um elemento
print(numeros)

numeros.remove(3)#remove um elemento
print(numeros)

#remover o elemento so se ele existir
numeros.discard(3)
print(numeros)

numeros.clear#limpa o conjunto
print(numeros)

pares = {2, 4, 6, 8}
impares = {3, 5, 7, 9}

u = pares | impares#uniao
print(u)

p2 = {4, 5, 6}


i = pares & p2#interseccao
print(i)#4, 6


#diferença mais conhecida como complementar
# d é o complementar de pares para se tornar p3

p3 = {2, 6}

d = pares - p3#diferenca é pares menos p3
print(d)

p4 = {4, 6, 10}

print(pares ^ p4)