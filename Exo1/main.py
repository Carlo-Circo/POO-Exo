from voiture import Voiture
# Création de voitures en utilisant la classe Voiture.
v1 = Voiture("Renault", "Clio", 2019, 45000, 15000)
v2 = Voiture("Peugeot", "208", 2022, 12000, 18000)
# affichage d'un kilométrage parcourue et de la valeur éstimée.
v1.parcourir(500)
print(v1.kilometrage)
print(v1.estimer_valeur())
# Affichage des informations de la voiture.
v2.afficher()
# Affichage du nombre de voitures créées.
print(f' Nombre de voitures: {Voiture.nb_voitures}')

