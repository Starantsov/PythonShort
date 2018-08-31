import random

def inputList(l):
    size = int (input("Введите размер: "))
    i = 0
    for item in range(0,size):
        l.append(int(input(str(i) + ": ")))
        i+=1
    return l

def outputList(l):
    print("\n")
    for item in l:
        print(item, end=" ")

def bubleSort(l):
    size = len(l)
    for i in range(0,size - 1):
        for j in range(0,size - 1):
            if l[j] > l[j + 1]:
                l[j] , l[j+1] = l[j+1] , l[j]
    return l

def getEven(L):
    B = []
    for i in range(0,len(L)):
        if L[i] % 2 != 0 or L[i] == 1 and L[i] != 0:
            B.append(L[i])
    return B