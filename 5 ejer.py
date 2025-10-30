# la nota final es 40 % del primer examen + 60 % del segon examen

nota1 = int(input("Introduïx la nota del primer examen: "))
nota2 = int(input("¿Quina nota vols tindre este trimestre? "))


notafinal = (nota2 - 0.4 * nota1) / 0.6

print(
    f"Per a obtindre un {nota2} en el trimestre necessites un {notafinal} en el segon examen."
)
