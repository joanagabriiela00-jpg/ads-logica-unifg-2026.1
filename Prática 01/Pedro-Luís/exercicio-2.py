import os
os.system("cls" if os.name == "nt" else "clear")

print("-=-" * 10)
while True:
    try:    
        valor_hora = float(input("Digite o valor cobrado por hora de trabalho: "))
        if valor_hora <= 0:
            print("Você não vai ganhar nada assim chefe!")
            continue
    except ValueError:
        print("DIGITE APENAS NÚMEROS!")
        continue
    break
while True:
    try:
        horas_concluir = int(input("Digite a estimativa em horas para conclusão do projeto: "))
        if horas_concluir <= 0:
            print("Tu não quer ganhar dinheiro mesmo né?")
            continue
    except ValueError:
        print("DIGITE APENAS NÚMEROS!")
        continue
    break

valor_total = valor_hora * horas_concluir
valor_total_impostos = valor_total + (valor_total * 0.15)

print("-=-" * 10)
print(f"O valor cobrado por hora é R$ {valor_hora:.2f}\nFaltam {horas_concluir} para conclusão do projeto\nO valor total com impostos é de R$ {valor_total_impostos:.2f}")