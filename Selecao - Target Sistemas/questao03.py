#QUESTÃO 03

faturamento_diario = [10000, 15000, 9000, 20000, 50000, 5500]
media_mensal = sum(faturamento_diario)/len(faturamento_diario)

print(f"O menor faturamento diário foi R${(min(faturamento_diario)):.2f} ")
print(f"O maior faturamento diário foi R${(max(faturamento_diario)):.2f} ")

dias_bons = 0
for dia in faturamento_diario:
    if dia >= media_mensal:
        dias_bons += 1

print(f"Média mensal: {media_mensal:.2f}")
print(f"O número de dias que superaram a média mensal foi: {dias_bons} dias ")