class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher(self):
        print(f"{self.nom} ({self.age} ans)")

class Chien(Animal):
    def __init__(self,nom, age, race):
        super().__init__(nom, age)
        self.race = race

    def afficher(self):
        super().afficher()
        print(f"La race du chien est {self.race}")
