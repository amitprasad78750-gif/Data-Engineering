UserList = []

def enterUser():


    for i in range(10):
        userName =input("Please Enter the ten user name ")
        UserList.append(userName)

    findNameGraetethyansix(UserList)



def findNameGraetethyansix(nameLst):

    for i in nameLst:
        if i.__len__() > 6:
            print(i ,"The Length of name is greater than 6")

        else:
            print(i,"The name is less than six digit")


enterUser()
