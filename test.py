def printPrime(range1, range2):
    flag = 0
    for num in range(range1, range2):
        for i in range(2, num/2):
            if(num%i==0):
                flag= 1
                break
            else:
                flag=0
        if(flag==0):
            print(num)
printPrime(100,500)