l = [34,"sd",65,12]


def printList():
    i = 0
    while i < len(l):
        print(l[i],end=", ") 
        i+=1
    print("\n")


printList()
l = l[::2]
printList()
