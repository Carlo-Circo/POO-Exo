clavier = ProduitElectronique("KB-001", "Clavier", 79.99, 15, 24, 0.5)

# Bug 1 : retourne False alors que clavier EST un Produit
if isinstance(clavier, Produit):
    print("C'est un produit")

# Bug 2 : ne détecte pas les sous-classes
def appliquer_remise(produit):
    if isinstance(produit, Produit):
        return produit.prix_ht * 0.9
    return produit.prix_ht   # jamais de remise pour ProduitElectronique !

# Bug 3 : fragile si on ajoute ProduitBricolage
for p in panier:
    if isinstance(p, (ProduitElectronique, ProduitAlimentaire)):
        p.afficher_details()