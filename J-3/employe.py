class Employe:
    def __init__(self, nom, salaire_base):
        self.nom          = nom
        self.salaire_base = salaire_base

    def calculer_prime(self):
        return 0   # pas de prime par défaut
    
class Commercial(Employe):
    def calculer_prime(self):
        return self.salaire_base * 0.15
    
class Technicien(Employe):
    def calculer_prime(self):
        return self.salaire_base * 0.10 + 200
    
salarie = [Employe("Marc", 2000), Commercial("Sophie", 2500), Technicien("Lucas", 2200)]

for p in salarie:
    print(f"{p.nom} a une prime de {p.calculer_prime():.0F} euros.")

total = sum(p.calculer_prime() for p in salarie)
print(f"Le total des primes est de {total:.0f}€.")