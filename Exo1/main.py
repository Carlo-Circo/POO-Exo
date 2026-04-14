from voiture import Voiture

v1 = Voiture("Renault", "Clio", 2019, 45000, 15000)
v2 = Voiture("Peugeot", "208", 2022, 12000, 18000)

v1.parcourir(500)
print(v1.kilometrage)
print(v1.estimer_valeur())

v2.afficher()

print(f' Nombre de voitures: {Voiture.nb_voitures}')

