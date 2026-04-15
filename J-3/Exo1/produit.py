from abc import ABC, abstractmethod

class Produit(ABC):
    tva = 20

    def __init__(self, reference, nom, prix_ht, stock):
        self.reference = reference      # public, assigné 1 fois à la création
        self.nom       = nom              # déclenche nom.setter ✓
        self.prix_ht   = prix_ht          # déclenche prix_ht.setter ✓
        self.stock     = stock            # déclenche stock.setter ✓

    @abstractmethod
    def calculer_frais_livraison(self):
        pass

    @abstractmethod
    def afficher_details(self):
        pass

    def afficher(self):
        print(f"[{self.reference}] {self.nom} : {self.prix_ht}€ HT")

    # ── nom ──────────────────────────────────────────

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, valeur):
        if not isinstance(valeur, str):
            raise TypeError("Le nom doit être une chaîne")
        if not valeur.strip():
            raise ValueError("Le nom ne peut pas être vide")
        self._nom = valeur.strip()

    # ── prix_ht ──────────────────────────────────────

    @property
    def prix_ht(self):
        return self._prix_ht

    @prix_ht.setter
    def prix_ht(self, valeur):
        if isinstance(valeur, bool):
            raise TypeError("Pas de booléen pour le prix")
        if not isinstance(valeur, (int, float)):
            raise TypeError("Le prix doit être un nombre")
        if valeur <= 0:
            raise ValueError("Le prix doit être positif")
        self._prix_ht = round(valeur, 2)

    # ── stock ────────────────────────────────────────

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valeur):
        if isinstance(valeur, bool):
            raise TypeError("Pas de booléen")
        if not isinstance(valeur, int):
            raise TypeError("Le stock doit être un entier")
        if valeur < 0:
            raise ValueError("Stock négatif interdit")
        self._stock = valeur

    # ── prix_ttc (lecture seule) ─────────────────────

    @property
    def prix_ttc(self):
        return round(self._prix_ht * (1 + Produit.tva / 100), 2)