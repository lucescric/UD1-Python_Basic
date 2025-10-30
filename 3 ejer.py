# Declarem variable
niño = int(input("Cuantos niños hay en el colegio? "))
niña = int(input("Cuantas niñas hay en el colegio? "))

# Calculem
Total = niño + niña

# Porcentaje
porcentajeniño = (niño / Total) * 100
porcentajeniña = (niña / Total) * 100

# Mostrar resultats
print(f"El porcentaje de niños es: {porcentajeniño:.2f} %")
print(f"El porcentaje de niñas es: {porcentajeniña:.2f} %")
