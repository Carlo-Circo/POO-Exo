class Temperature:
    def __init__ (self, temperature_celsius):
        self.temperature_celsius = temperature_celsius
    
    @property
    def temperature_celsius(self):
        return self._temperature_celsius
    
    @temperature_celsius.setter
    def temperature_celsius(self, valeur):
        if isinstance(valeur, bool):
            raise TypeError("Pas de booléen pour la température")
        if not isinstance(valeur, (int, float)):
            raise TypeError("La température en celsius doit être un nombre")
        if valeur < -273.15:
            raise ValueError("En dessous du zéro absolu")
        if valeur > 1000000:
            raise ValueError("Température")
        self._temperature_celsius = round(valeur, 2)
    
    @property
    def fahrenheit(self):
        return round (self._temperature_celsius * 9 / 5 + 32, 2)
    
    @property
    def kelvin(self):
        return round (self._temperature_celsius + 273.15, 2)
    
    @property
    def etat(self):
        if self._temperature_celsius <= 0:
            return "solide"
        if self._temperature_celsius > 0 and self._temperature_celsius <= 100:
            return "liquide"
        if self._temperature_celsius > 100:
            return "gazeux"
    
    @classmethod
    def depuis_fahrenheit(cls, valeur_f):
        Celsius = (valeur_f - 32) * 5 / 9
        return cls(round(Celsius, 2))
    
    def est_compatible_avec(self, autre):
        return self.etat == autre.etat