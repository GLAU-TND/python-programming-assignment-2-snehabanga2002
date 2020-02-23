n = int(input())
a = bin(n)[2:]
b = list(map(str,a.split("0")))
y = 0
for i in b:
    x = len(i)
    if x > y:
        y = x
print(y)


INPUT:
    156
OUTPUT:
    3
