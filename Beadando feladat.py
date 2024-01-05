import random
lst = []
i = 0
n = 20
v = 0
print("1.feladat")
print("")
while i < n:
    x = random.randint(-10,10)
    v += x
    lst.append(x)
    i += 1
print(lst)
print("")
print("2.feladat")
print("")
for i in range(n//2):
    s = lst[i]
    lst[i] = lst[n - 1 - i]
    lst[n - 1 - i] = s 
print(lst)

print("")
print("3.feladat")
print("")
print(v)
print("")
if v%3 == 0:
    print("Osztható hárommal.")
else:
    print("Nem osztható hárommal.")
i = 1
a = 0
print("4.feladat")
while i < n-1:
    if lst[i] == lst[i-1]+lst[i+1]:
        print(lst[i])
