# Sense executar el programa, ¿que s’imprimix per consola?

print(str(123456 // 10) + " " + str(123456 % 10))
print(str(123456 // 100) + " " + str(123456 % 100))
print(str(123456 // 1000) + " " + str(123456 % 1000))
print(str(123456 // 10000) + " " + str(123456 % 10000))
print(str(123456 // 100000) + " " + str(123456 % 100000))

# Resposta:
# 12345 6
# 1234 56
# 123 456
# 12 3456
# 1 23456
# Explicació:
# El operador '//' realitza una divisió entera, eliminant qualsevol part decimal, mentre que l'operador '%' retorna el residu de la divisió.
# Per exemple, en la primera línia:
# 123456 // 10 = 12345 (divisió entera de 123456 per 10)
# 123456 % 10 = 6 (residu de la divisió de 123456 per 10)
# Aquest patró es repeteix en les línies següents, amb el divisor augmentant en potències de 10.

# A la vista dels resultats obtinguts, ¿pot tindre alguna utilitat?

# Sí, aquesta tècnica pot ser útil per descompondre un nombre en les seves xifres individuals.
# Per exemple, si es vol analitzar o manipular cada xifra d'un nombre (com en aplicacions de processament de números, verificació de dígits, etc.),
# aquesta metodologia permet accedir fàcilment a cada xifra per separat.
