populacao_a = 80000
populacao_b = 200000

taxa_a = 0.03
taxa_b = 0.015
anos = 0 

while populacao_a < populacao_b: 
    populacao_a = populacao_a + (populacao_a * taxa_a)
    populacao_b = populacao_b + (populacao_b * taxa_b)
    anos = anos + 1

print("Serao necessarios ", anos, " anos para a populacao A ultrapassar a populacao B.")