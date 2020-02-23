a = bin(int(input()))[2:];
b = list(map(str,a.split("0")))
ans = 0
for i in b:
    temp = len(i)
    if temp > ans:
        ans = temp
print(ans)


INPUT:
    156
OUTPUT:
    3
