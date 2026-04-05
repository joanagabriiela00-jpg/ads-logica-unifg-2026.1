import os
os.system("cls" if os.name == "nt" else "clear")

print("-=-" * 10)
while True:
    try:    
        pizza_fatias = int(input("Digite a quantidade de fatias: "))
        if pizza_fatias <=0:
            print("Então tu n pedisse uma pizza")
            continue
    except ValueError:
        print("DIGITE APENAS NÚMEROS!")
        continue
    break
while True:
    try:
        programadores = int(input("Digite a quantidade de programados que vão comer a pizza: "))
        if programadores <=0:
            print("Então nem tem pizza.")
            continue
    except ValueError:
        print("DIGITE APENAS NÚMEROS!")
        continue
    break
fatias_por_pessoa = pizza_fatias // programadores
sobra = pizza_fatias % programadores

print(f"Todos os {programadores} programadores irão comer {fatias_por_pessoa} fatias cada um.\nE irá sobrar {sobra} pizzas.")
