# Determinar el valor, true o false, de cada una de las siguientes expresiones lógicas, asumiendo que el valor de las variables cont y limit es 10 y 20, respectivamente.

# a) (cont == 0) && (limit < 20)

# false && false -> false

# b) (limit >=20)  || (cont < 5)

# true || false -> true

# c) ((limit / (cont-10)) > 7) || (limit < 20)

# Error de división por cero -> false ninguna de las dos condiciones se cumple

# d) (limit <= 20) || ((limit/(cont-10)) > 7)

# true || Error de división por cero -> true porque cumple la primera condición

# e) ((limit / (cont-10)) > 7) && (limit < 0)

# Error de división por cero -> false ninguna de las dos condiciones se cumple

# f) (limit < 0) && ((limit / (cont-10)) > 7)

# false && Error de división por cero -> false porque no se cumple la primera condición y debe complir ambas
