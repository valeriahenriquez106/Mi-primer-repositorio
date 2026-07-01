a, b = 48, 18

x = a
y = b

while y != 0:
    residuo = x % y
    x = y
    y = residuo

mcd = x

print("El MCD de", a, "y", b, "es:", mcd)
