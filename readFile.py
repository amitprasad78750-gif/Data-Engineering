class readFile:
    def fileRead(self):
        path="C:/Users/Amit Kumar Prasad/Desktop/abc.txt"

        with open(path, "r") as file:
            content = file.read()
            print(content)



obj1= readFile()
obj1.fileRead()            