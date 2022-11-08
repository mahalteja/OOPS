class student:
    #To make variable or Method to private type we have to put __ infront of the variable
    def __init__(self,name,age):
        self.__name=name
        self.age=age
    def setdata(self,name):
        self.__name=name
        #Here we are changing the value of the private values to get acess from outside of class
    def showdata(self):
        print(self.__name)
s1=student('Mahal',20)
s1.setdata('NO')
s1.showdata()
