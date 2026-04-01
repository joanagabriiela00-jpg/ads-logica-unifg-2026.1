import os
os.system("cls" if os.name == "nt" else "clear")


while True:
    try:
        idade = int(input("Digite a sua idade: "))
        if idade <= 0:
            print("Você nem existe pô.")
            continue
    except ValueError:
        print("DIGITE APENAS NÚMEROS!")
        continue
    break
while True:
    try:
        experiencia = int(input("Digite a sua experiencia com programação: "))
        if experiencia < 0:
            print("Não tem como ter experiencia negativa amigão.")
            continue
    except ValueError:
        print("DIGITE APENAS NÚMEROS!")
        continue
    break

acesso = (idade >= 18) and (experiencia > 2)
print("-=-" * 10)
print(f"O seu acesso é {acesso}")