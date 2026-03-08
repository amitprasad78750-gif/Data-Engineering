
class fibonnaci:

    def fiboseries(self,a,b,n):
        print(a,b,end="  ")
        while(n > 0):
            a,b=b,a+b
            print(b,end =" ")
            n -=1




fibonnaci().fiboseries(0,1,10)





