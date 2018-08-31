listStudents = [["Nazar","Anton","Egor"], [10,20,30]]
 
listStudents[0].append("Gosha")
listStudents[1].append(2)

i=0
while i < len(listStudents[0]):
    print("Name: ",listStudents[0][i], "\nMark: ", listStudents[1][i], "\n")
    i+=1

i=0
findName = input("Search pupil: ")

for name in listStudents[0]:
    if findName == name:
        print("\nSuccess!!!")
        print("Name: ",listStudents[0][i], "\nMark: ", listStudents[1][i], "\n")
        break
else:
    print("Pupil is not found...")