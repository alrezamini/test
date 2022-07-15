a = int(input())
flg = False
for x in range(1,100):
    if flg == True:
        print(x)
        break
    temp = x * a
    while temp > 0:
        if temp / 10 == 1:
            flg = True
            temp = temp%10
        else:
            flg = False
            break