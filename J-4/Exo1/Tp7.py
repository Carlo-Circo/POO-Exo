class Produit:
    tva = 20
    
    def __init__(self, nom, reference, prix_ht):
        self._nom  = nom
        self._reference = reference
        self._prix_ht = prix_ht
    
    def __str__(self):
        return f"{self._nom} ({self._reference}) - {self._prix_ht}€ HT"
    
    def __repr__(self):
        return f"Produit('{self._reference}', '{self._nom}', {self._prix_ht})"

    def __eq__(self, other):
        if not isinstance(other, Produit): return False
        return self._reference == other._reference
    
    def __lt__(self, other):
        return self._prix_ht < other._prix_ht

    def __hash__(self):
        return hash(self._reference)
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["ref"], data["nom"], data["prix"])
    
    @staticmethod
    def valider_prix(prix):
        if isinstance (prix, bool): return False
        return isinstance (prix, (int, float)) and prix > 0

p1 = Produit("KB-001", "Clavier", 79.99)
p2 = Produit.from_dict({"ref": "MS-001", "nom": "Souris", "prix": 49.99})
p3 = Produit("KB-001", "Clavier v2", 89.99)

print(p1)
print(repr(p1))
print(p1 == p3)
print(p1 < p2)

tries = sorted([p1, p2])
print([str(p) for p in tries])

catalogue = {p1, p2, p3}
print(len(catalogue))        # 2

print(Produit.valider_prix(49.99))  # True
print(Produit.valider_prix(-10))   # False