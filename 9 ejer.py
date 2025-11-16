# Exercici teòric
# Si s’executa el següent bloc d’instruccions, ¿es produïx una divisió per zero?

j = -2
b = (j > 0) and (1 / (j + 2) > 10)

print(b)


# Resposta: No, no es produeix una divisió per zero.
# Explicació: En Python, l'operador 'and' utilitza avaluació curta (short-circuit evaluation).
# Això significa que si la primera condició (j > 0) és falsa, la segona condició no s'avalua i, per tant, no es produeix la divisió per zero.
# En aquest cas, com que j és -2, la primera condició (j > 0) és falsa, així que Python no intenta avaluar (1 / (j + 2)), evitant així qualsevol divisió per zero.
