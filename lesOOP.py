class Person:
    _Name = ""
    _Age = ""
    def __init__(self,name,age):
        self.Name = name
        self.Age = age

    def outPut(self):
       return "Name: " + self.Name + "\n" + "Age: " + self.Age + "\n" 

class Student(Person):
    Course = ""
    def __init__(self,name,age,course):
        self.Name = str(name)
        self.Age = str(age)
        self.Course = str(course)

    def outPut(self):
       return "Name: " + self.Name + "\n" + "Age: " + self.Age + "\n" + "Course: "+ self.Course

    def __eq__(self,other):
        return self.Name == other.Name
        

Ivan = Person("Ivan", "18")
print (Ivan.outPut())
IvanS = Student("Ivan", "18","2")
print (IvanS.outPut())
print(IvanS == Ivan)