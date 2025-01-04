# Primero se ejecutan las operaciones entre paréntesis, 
# luego las potencias, luego multiplicaciones y divisiones, 
# y por último sumas y restas. 
# En caso de tener operaciones con la misma prioridad,
# se ejecutan de izquierda a derecha.

# Ejemplo:
a = 2 + 3 * 4
b = (2 + 3) * 4
c = 2 + 3 * 4 ** 2

print(a)  # 14
print(b)  # 20
print(c)  # 50
