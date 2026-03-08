
class A:
    def __init__(self):
        print("in a INIT")
    def feature(self):
        print("feature 1 is running")

    def feature2(self):
        print("feature 2 is running")


class B(A):
    def __init__(self):
        print("")
    def feature3(self):
        print("feature 3 is running")

    def feature4(self):
        print("feature 4 is running ")

class C(A,B):
    def feature4(self):
        print("feature 5 is running")

s1=A()