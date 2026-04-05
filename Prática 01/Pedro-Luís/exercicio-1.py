import os
os.system("cls" if os.name == "nt" else "clear")

print("-=-" * 10)
while True:
    nome = input("Digite o seu nome: ").title().replace(" De ", "de").replace(" Da ", "da").replace(" Do ", "do")
    if not nome.replace(" ", "").isalpha():
        print("Digite apenas letras no seu nome!")
        continue
    break
while True:
    try:
        ano_nascimento = int(input("Digite a sua data de nascimento: "))
        if ano_nascimento <= 1899:
            print("Ano inválido!")
            continue
    except ValueError:
        print("DIGITE APENAS NÚMEROS!")
        continue   
    break
while True:
    try:
        altura = float(input("Digite a sua altura: "))
        if altura <= 0.1:
            print("Com essa altura você não existe!")
            continue
    except ValueError:
        print("DIGITE APENAS NÚMEROS!")
        continue
    break
idade = 2026 - ano_nascimento
print("-=-" * 10)
print(f"Olá, {nome}! Você tem {idade} anos e sua altura é de {altura} M. Registro concluido.")