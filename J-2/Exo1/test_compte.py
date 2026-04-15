from compte_securise import CompteBancaire

c = CompteBancaire("Alice", 500, 200)

c.deposer(100)          # Dépôt de 100. Nouveau solde : 600
c.retirer(800)          # Retrait de 800. Nouveau solde : -200
c.retirer(50)           # Opération refusée — découvert dépassé

print(c.solde)           # -200
print(c.est_a_decouvert)  # True
print(c.nb_operations)   # 2 (seules les opérations réussies comptent)

c.afficher_historique()
# Historique de Alice :
#   + 100 | solde : 600
#   - 800 | solde : -200

c.titulaire = ""         # ValueError
c.deposer(True)          # TypeError — pas de booléen