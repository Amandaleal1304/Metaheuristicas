
populacao_a =float(input("População A: "))
populacao_b = float(input("População B: "))



taxa_a = float(input("Taxa de crescimento A: "))
taxa_b = float(input("Taxa de crescimento B: "))

anos = 0 

while populacao_a < populacao_b: 
    populacao_a = populacao_a + (populacao_a * taxa_a)
    populacao_b = populacao_b + (populacao_b * taxa_b)
    anos = anos + 1

print("Serao necessarios ", anos, " anos para a populacao A ultrapassar a populacao B.")