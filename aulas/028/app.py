try:
    idade = int(input("idade: "))
    print(f"Você tem {idade} anos.")
except ValueError:
    print("Idade inválida.")
