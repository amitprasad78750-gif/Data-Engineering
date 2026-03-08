
class Palindrome:
    def checking(self,name):
        chkpalin = True
        totalcount=len(name)-1
        for i in range(len(name)):
            if name[i]!=name[totalcount]:
                chkpalin = False
                break
            else:
                totalcount -=1
                continue
        return chkpalin

nameList = "ram"
MyCheck=Palindrome().checking(nameList)
print(MyCheck)


