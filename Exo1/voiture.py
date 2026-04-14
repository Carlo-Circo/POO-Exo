#Classe Voiture
class Voiture:
    # Initialisation de l'attribut de classe pour compter le nombre de voitures créees.
    nb_voitures = 0
    # attributs: marque, modele, annee, kilometrage, prix_neuf
    def __init__(self, marque, modele, annee, kilometrage, prix_neuf):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.prix_neuf = prix_neuf
        Voiture.nb_voitures += 1
    # Méthodes
    def afficher(self):
        print(f" Marque: {self.marque}")
        print(f" Modèle: {self.modele}")
        print(f" Année: {self.annee}")
        print(f" Kilométrage: {self.kilometrage}")
        print(f" Prix neuf: {self.prix_neuf}")
    # Méthode pour vérifier si la voiture est récente
    def est_recente(self):
        return self.annee >= 2020
    # Méthode pour parcourir une distance et mettre à jour le kilomètrage.
    def parcourir(self,distance):
        self.kilometrage += distance
    # Méthode pour estimer la valeur de la voiture en fonciton du kilomètrage.
    def estimer_valeur(self):
        return self.prix_neuf - (self.kilometrage * 0.05)
    