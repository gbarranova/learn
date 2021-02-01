x = int(input("Height "))
if(x > 0):
    y = x-1
    for i in range(x):
        for j in range(y):
            print(" ", end = "")
        for j in range(i+1):
            print("#", end = "")
        print("  ", end = "")
        for j in range(i+1):
            print("#", end = "")
        print()
        y -= 1
else:
    print("ta errado apaga tudo")