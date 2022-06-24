#QUESTÃO 04

SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
outros = 19849.53

total = SP + RJ + MG + ES + outros

porcentagem_SP = (SP/total)*100
porcentagem_RJ = (RJ/total)*100
porcentagem_MG = (MG/total)*100
porcentagem_ES = (ES/total)*100
porcentagem_outros = (outros/total)*100

print(f"SP representa {porcentagem_SP:.2f}% do faturamento mensal")
print(f"RJ representa {porcentagem_RJ:.2f}% do faturamento mensal")
print(f"MG representa {porcentagem_MG:.2f}% do faturamento mensal")
print(f"ES representa {porcentagem_ES:.2f}% do faturamento mensal")
print(f"OS outros representam {porcentagem_outros:.2f}% do faturamento mensal")