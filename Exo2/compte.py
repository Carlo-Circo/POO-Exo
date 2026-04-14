# Création de la classe CompteBancaire
class CompteBancaire:
    # Initialisation de l'attibut de classe decouvert_autorise
    decouvert_autorise = 0
    # attributs: titulaire, solder, decouvert_autorise, historique
    def __init__(self, titulaire, solde, decouvert_autorise):
        self.titulaire = titulaire
        self.solde = solde
        self. decouvert_autorise = decouvert_autorise
        self.historique = []
    # Méthodes déposer montant + ajouter a l'historique.
    def deposer(self, montant):
        self.solde += montant
        self.historique.append(f"Dépôt de {montant}€")
    # Méthode retirer montant + vérifier si le solde est suffisant et ajouter à l'historique.
    def retirer(self, montant):
        if self.solde - montant <= self.decouvert_autorise:
            self.solde -= montant
            self.historique.append(f"Retrait de {montant}€")
        else:
            print("Opération refusée")
    # Méthode virement vers un autre compte + vérifier si le solde est suffisant et ajouter à l'historique des deux comptes.
    def virement(self, autre_compte, montant):
        if self.solde - montant >= - self.decouvert_autorise:
            self.solde -= montant
            autre_compte.solde += montant
            self.historique.append(f"Virement de {montant}€ vers {autre_compte.titulaire}")
            autre_compte.historique.append(f"Virement de {montant}€ reçu de {self.titulaire}")
        else:
            print("Opération refusée")
    # Méthode pour afficher l'historique complet du compte.
    def afficher_historique(self):
        print(f"Historique du compte de {self.titulaire} :")
        for operation in self.historique:
            print (operation)
        print(f"solde : {self.solde}€")
    # Méthode pour appliquer les intérêts sur le solde du compte + vérifier si le solde est positif et ajouter à l'historique.
    def appliquer_interets(self, taux_interet):
        if self.solde > 0:
            interets = self.solde * taux_interet
            self.solde =+ interets
            self.historique.append(f"Intérêts de {interets}€ appliqués")
        else:
            print("opération refusée")
            