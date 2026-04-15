from temperature import Temperature

t1 = Temperature(22.5)
print(t1.fahrenheit)          # 72.5
print(t1.kelvin)              # 295.65
print(t1.etat)                # liquide

t2 = Temperature.depuis_fahrenheit(32)
print(t2._temperature_celsius)      # 0.0 → solide

print(t1.est_compatible_avec(t2))  # False (liquide vs solide)

t3 = Temperature(50)
print(t1.est_compatible_avec(t3))  # True (liquide vs liquide)

Temperature(-300)              # ValueError — zéro absolu
Temperature(True)              # TypeError — pas de booléen
