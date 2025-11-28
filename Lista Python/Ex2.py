total = 20.00
idade = int(input("Digite a idade da pessoa: "))

if idade < 12 or idade > 60:
    pagar = total * 0.5
    print("A pessoa tem direito ao desconto.")
else:
    pagar = total
    print("A pessoa não tem direito ao desconto.")

print(f"O valor a ser pago pelo ingresso é: R$ {pagar:.2f}")