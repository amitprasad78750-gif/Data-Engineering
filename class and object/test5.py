
class Student:

    school ='Jons School'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1


    def set_m1(self,value):
        self.m1 = value
    @classmethod
    def get_School(cls):
        return cls.school
    @staticmethod
    def info():
        print("This is student class in module ")


s1= Student(30,40,50)
s2 = Student(60,70,80)




print(s1.info())



