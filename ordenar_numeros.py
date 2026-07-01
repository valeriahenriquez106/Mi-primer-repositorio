a, b, c = 15, 8, 22

if a > b:
    temporal = a
    a = b
    b = temporal

if b > c:
    temporal = b
    b = c
    c = temporal

if a > b:
    temporal = a
    a = b
    b = temporal

print("Números ordenados de menor a mayor:", a, b, c)
