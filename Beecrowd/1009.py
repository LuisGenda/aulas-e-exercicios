nome = input()
salario = float(input())
vendas = float(input())

total_receber = salario + (vendas * 0.15)

print(f"TOTAL = R$ {total_receber:.2f}")
