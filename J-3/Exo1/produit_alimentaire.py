from produit import Produit
from datetime import date

class ProduitAlimentaire(Produit):
    def __init__(self, reference, nom, prix_ht, stock, date_peremption):
        super().__init__(reference, nom, prix_ht, stock)
        self.date_peremption = date_peremption

    @property
    def date_peremption(self):
        return self._date_peremption
    
    @date_peremption.setter
    def date_peremption(self, valeur):
        if isinstance(valeur, date):
            self.date_peremption = valeur
        if not isinstance (valeur, str):
            raise TypeError ("La date de peremption doit être une chaine ISO ! (YYYY-MM-DD)")
        self._date_peremption = date.fromisoformat(valeur)
    
    def est_perime(self):
        self.date_peremption < date.today()
    
    def calculer_frais_livraison(self):
        return 15.00
    
    def afficher_details(self):
        dtatut = "Périmé !" if self.est_perime() else "OK"
        print(f" Date de péremption : {self._date_peremption}")
        