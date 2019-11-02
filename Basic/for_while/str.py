a = input()
b = input()


temp = 0
if(len(a) == len(b)):
    for i in range(len(b)):
        if(a[0] == b[i]):
            temp = 1
            break
        if(a[1] == b[i]):
            temp = 2
            break
    if(temp == 0):
        print("str False")
    elif(temp == 1 or 2):
        print("str Ture")


