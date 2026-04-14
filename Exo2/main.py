from compte import CompteBancaire

c1 = CompteBancaire("Alice", 500, 200)
c2 = CompteBancaire("Bob", 200, 0)


c1.retirer(650)
c1.virement(c2, 100)


c2.virement(c1, 50)
print(c1.solde)
print(c2.solde)


c2.afficher_historique()
