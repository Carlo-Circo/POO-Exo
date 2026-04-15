# Création de la classe CompteBancaire
class CompteBancaire:
    # Initialisation de l'atribut de classe decouvert_autorise
    decouvert_autorise = 0
    # attributs: titulaire, solde, decouvert_autorise, historique
    def __init__(self, titulaire, solde = 0, decouvert_autorise = 0):
        self.historique = []
        self._titulaire = titulaire
        self._decouvert_autorise = decouvert_autorise
        self._solde = solde
    #Titulaire
    @property
    def titulaire(self):
        return self._titulaire
    @titulaire.setter
    def titulaire(self, valeur):
        if not isinstance(valeur, str):
            raise TypeError("Le nom doit être une chaîne")
        if not valeur.strip():
            raise ValueError("Le nom ne peut pas être vide")
        self.nom = valeur.strip()
    # Découvert autorisé
    @property
    def decouvert_autorise(self):
        return self._decouvert_autorise
    
    @decouvert_autorise.setter
    def decouvert_autorise(self,valeur):
        if isinstance (valeur, bool):
            raise TypeError("Pas de booléen")
        if not isinstance(valeur, (int, float)):
            raise TypeError("le decouvert autorisé doit être un nombre")
        if valeur < 0:
            raise ValueError("Le decouvert ne peut pas être négatif")
        self._decouvert_autorise = valeur
    
    # Solde
    @property
    def solde(self):
        return self._solde
    
    @solde.setter
    def solde(self, valeur):
        if isinstance (valeur, bool):
            raise TypeError("Pas de booléen")
        if not isinstance (valeur, (int, float)):
            raise TypeError ("Le solde doit être un nombre")
        if valeur > -self.decouvert_autorise:
            raise ValueError ("Le découvert est dépassé !")
        self._solde = round (valeur, 2)

    # Propriété est a decouvert
    @property
    def est_a_decouvert(self):
        if self._solde < 0:
            return True
    
    # Propriété nombre d'opérations
    @property
    def nb_operations(self):
        return len(self.historique)
    
    # Méthodes déposer montant + ajouter a l'historique.
    def deposer(self, montant):
        if isinstance (montant, bool):
            raise TypeError("Pas de booléen !")
        if not isinstance (montant, (int, float)):
            raise TypeError ("Le montant doit être un nombre.")
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")
        self._solde = round(self._solde + montant, 2)
        self.historique.append({"type": "depot", "montant": montant, "solde": self.solde})
        print(f"Dépôt de {montant}. Nouveau solde : {self.solde}")

    # Méthode retirer montant + vérifier si le solde est suffisant et ajouter à l'historique.
    def retirer(self, montant):
        if isinstance(montant, bool):
            raise TypeError("Pas de booléen !")
        if not isinstance (montant, (int, float)):
            raise TypeError ("Le montant doit être un nombre.")
        if montant <= 0:
            raise ValueError ("Le montant doit être positif.")
        if self._solde - montant < -self._decouvert_autorise:
            print("Vous avez dépassé votre découvert, opération refusée")
            return False
        self._solde = round(self._solde - montant, 2)
        self.historique.append({"type": "retrait", "montant": montant, "solde": self._solde})
        print(f"Retrait de {montant}. Nouveau solde : {self._solde}")
        return True
    
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
            signe_operation = "+" if operation["type"] == "depot" else "-"
            print (f"{signe_operation}{operation['montant']}€, Solde : {operation['solde']}€")
        print(f"solde : {self.solde}€")
    # Méthode pour appliquer les intérêts sur le solde du compte + vérifier si le solde est positif et ajouter à l'historique.
    def appliquer_interets(self, taux_interet):
        if self.solde > 0:
            interets = self.solde * taux_interet
            self.solde =+ interets
            self.historique.append(f"Intérêts de {interets}€ appliqués")
        else:
            print("opération refusée")