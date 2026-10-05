def quadrado(numero):
    return numero * numero
num_digitado = int(input("Digite um número: "))
valor = quadrado(num_digitado)

print(f"O resultado do quadrado de {num_digitado} é {valor}")