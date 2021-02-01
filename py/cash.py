while True:
    x = float(input("Change owed: "))
    x = x*100
    x = int(x)
    y = int(0)
    while(x >= 25):
        x -= 25 
        y += 1
    while(x >= 10):
        x -= 10 
        y += 1
    while(x >= 5):
        x -= 5 
        y += 1
    while(x >= 1):
        x -= 1
        y += 1
 
    print(y)