x = int(input("Height "))
y = x-1
for i in range(x):
    for j in range(y):
        print(" ", end = "")
    for j in range(i+1):
        print("#", end = "")
    print()
    y -= 1