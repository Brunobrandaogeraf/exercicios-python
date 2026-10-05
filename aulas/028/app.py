while True:
    try:
        
        idade = int(input("idade: "))
        salario = 10000
        risco = salario/idade
        print(f"Você tem {idade} anos.")
        break #Sai do loop se não houver exceções
    except ValueError:
         print("Idade inválida.")
    except ZeroDivisionError:
         print("Idade não pode ser zero.")
