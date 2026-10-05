# Classes
# Métodos= comportamento
# Atributos = caracteristicas

lista =[1,2,3,4,5]
class Aluno:
    def aprovar(self):
        print("Aprovado")

    def reprovar(self):
        print("Reprovado")
aluno1 = Aluno()
aluno2 = Aluno()
aluno1.nome = "Maria"
aluno2.nome = "João"
aluno1.idade = 10
aluno2.idade = 15
print(f"{aluno1.nome} tem {aluno1.idade} anos e está")
aluno1.aprovar()
print(f"{aluno2.nome} tem {aluno2.idade} anos e está")
aluno2.reprovar()