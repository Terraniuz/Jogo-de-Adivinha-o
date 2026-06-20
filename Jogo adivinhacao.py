import random

numero = random.randint(1, 100)

while True:
    chute = int(input("Adivinhe o número: "))

    if chute == numero:
        print("Você acertou!")
        break
    elif chute < numero:
        print("Muito baixo!")
    else:
        print("Muito alto!")
