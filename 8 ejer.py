a, b, c = 12, 8, 6
print(a, b, c)
a = c
print(a, b, c)
c += b
print(a, b, c)
a = b + c
print(a, b, c)
a += 1
b += 1
print(a, b, c)
c = a + b
a += 1
b += 1
print(a, b, c)
