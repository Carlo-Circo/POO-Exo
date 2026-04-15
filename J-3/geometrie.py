from abc import ABC, abstractmethod
import math

class Forme(ABC):
    def __init__(self, couleur):
        self.couleur = couleur

    @abstractmethod
    def aire(self):
        """Retourne l'aire de la forme"""
        pass

    @abstractmethod
    def perimetre(self):
        """Retourne le périmètre de la forme"""
        pass

    def afficher(self):       # méthode concrète : héritée telle quelle
        print(f"{self.__class__.__name__} ({self.couleur})")
        print(f"  Aire      : {self.aire():.2f}")
        print(f"  Périmètre : {self.perimetre():.2f}")

    def Rectangle(Forme):
        def __init__(self, couleur, largeur, hauteur):
            super().__init__(couleur)
            self.Largeur = largeur
            self.Hauteur = hauteur
        
        def aire(self):
            return self.Largeur * self.Hauteur
        
        def perimetre(self):
            return 2 * (self.Largeur + self.Hauteur)
        
    def Cercle(forme):
        def __init__(self, couleur, rayon):
            super().__init__(couleur)
            self.Rayon = rayon
        
        def aire(self):
            return math.pi * self.Rayon ** 2
        
        def perimetre(self):
            return 2 * math.pi * self.Rayon
        
        