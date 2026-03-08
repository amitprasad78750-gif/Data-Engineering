

class Student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()


    def show(self):
        print(self.name,self.rollno)

    class Laptop:
        def __init__(self):
            self.brand ='HP'
            self.cpu ='i5'
            self.ram = 8


s1=Student('amit',1)
s1.show()

lap1=s1.lap
print(lap1.brand)

lap2=Student.Laptop()
print(lap2.cpu)