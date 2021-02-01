while True:
    number = input("Number: ")
    firstdigits = 0
    legit = False
    x = int(number)
    suma = 0
    while (x > 9):
        x = int(x/10)
        temp = int(x % 10)
        temp = temp*2
        if temp > 9:
            temp = int(temp/10) + int(temp % 10)
        x = int(x/10)
        suma = suma + temp
    y = int(number)
    temp = 0
    sumb = 0
    while (y > 0):
        temp = int(y % 10)
        y = int(y/100)
        sumb = sumb + temp
    sumt = suma + sumb
    if ((sumt%10) == 0):
        legit = True


    numcard = int(number)
    if(legit == True):
        while(numcard > 99):
            numcard = int(numcard/10)


    if numcard in [34, 37]:
        print("AMEX")
    elif numcard in range(51, 56):
        print("MASTERCARD")
    elif(int(numcard/10) == 4):
        print("VISA")
    else:
        print("INVALID")