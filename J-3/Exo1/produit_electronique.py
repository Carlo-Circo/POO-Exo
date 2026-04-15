from produit import Produit

class ProduitElectronique(Produit):
    def __init__(self, reference, nom, prix_ht, stock, garantie_mois, poids_kg):
        super().__init__(reference, nom, prix_ht, stock)
        self.garantie_mois = garantie_mois
        self.poids_kg = poids_kg

    @property
    def garantie_mois(self):
        return self._garantie_mois
    
    @garantie_mois.setter
    def garantie_mois(self, valeur):
        if isinstance(valeur, bool):
            raise TypeError("Pas de booléen pour la garantie !")
        if not isinstance(valeur, int):
            raise TypeError("La garantie doit être un entier !")
        if valeur < 0:
            raise ValueError("La garantie doit être positive ou nulle !")
        self._garantie_mois = valeur

    @property
    def poids_kg(self):
        return self._poids_kg
    
    @poids_kg.setter
    def poids_kg(self, valeur):
        if isinstance(valeur, bool):
            raise TypeError("Pas de booléen pour le poids !")
        if not isinstance(valeur, (int, float)):
            raise TypeError("Le poids doit être un nombre !")
        if valeur <= 0:
            raise ValueError("Le poids doit être positif !")
        self._poids_kg = valeur

    def calculer_frais_livraison(self):
        return round(10.0 + self.poids_kg * 2, 2)
    
    def afficher_details(self):
        super().afficher()
        print(f"Garantie : {self.garantie_mois} mois | Poids : {self.poids_kg} kg")
