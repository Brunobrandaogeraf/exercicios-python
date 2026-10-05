# Classes
# Métodos= comportamento
# Atributos = caracteristicas

lista =[1,2,3,4,5]
class Aluno:
    def __init__(self, nome, idade, escola = "escola1"):
        self.nome = nome
        self.idade = idade
        self.escola = escola
    


    def aprovar(self):
        print("Aprovado")
    
    def reprovar(self):
        print("Reprovado")
aluno1 = Aluno("Ana", 15)
aluno2 = Aluno("João", 15)
print(aluno1.nome)
print(aluno1.idade)
print(aluno1.escola)

