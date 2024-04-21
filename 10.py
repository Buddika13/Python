x = input("Enter name")
a = len(x)
y = a // 2
if a % 2 == 0:
    print(x[y - 1] + x[y])
else:
    print(x[y])
