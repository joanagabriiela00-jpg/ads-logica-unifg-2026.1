import os
os.system("cls" if os.name == "nt" else "clear")

while True: 
    try:
        mega = int(input("Digite o tamanho do aquivo em Megabytes(MB): "))
        if mega <= 0:
            print("Então não tem arquivo.")
            continue
    except ValueError:
        print("DIGITE APENAS NÚMEROS!")
        continue
    break
while True:
    try:
        mb_por_segundo = int(input("Digite a velocidade de conexão da internet em Megabits por segundo(Mbps): "))
        if mb_por_segundo <= 0:
            print("Então não tem arquivo.")
            continue
    except ValueError:
        print("DIGITE APENAS NÚMEROS!")
        continue
    break

tempo_segundos = mega / (mb_por_segundo / 8)
minutos = tempo_segundos // 60
segundos_restantes = tempo_segundos % 60

print("-=-" * 13)
print(f"{minutos} minutos e {segundos_restantes} segundos para completar o download.")
