
class Animal:
    def passear(self):
        print("passear")

class Cachorro(Animal):
    def latir(self):
        print("latir")

class Gato(Animal):
    def miar(self):
        print("miar")

Caramelo1 = Cachorro()
Caramelo1.passear() 
Caramelo1.latir()
