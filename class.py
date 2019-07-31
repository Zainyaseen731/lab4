from numpy import *
class Student:

    # def __init__(self): #constructor
    #     self.id = 0
    #     self.name=" "
    #     self.quantity=0
    #     self.cost=0

    def __init__(self,id=0,name=" ",quantity=0,cost=0):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def setId(self,id): #for set the value of ID
        self.id=id

    def setName(self, name):  #for set the value of Name
        self.name = name

    def setQuan(self,quantity):  #for set the value of Quantity
        self.quantity=quantity

    def setCost(self,cost):  #for set the value of Cost
        self.cost=cost

    def getId(self): #for getting the value of ID
        return self.id

    def getName(self): #for getting the value of Name
        return self.name

    def getQuan(self): #for getting the value of Quantity
        return self.quantity

    def getCost(self): #for getting the value of Cost
        return self.cost

    def setItem(self,id,name,quantity,cost): #set all the values of a object
        self.id = id
        self.name=name
        self.quantity=quantity
        self.cost=cost

    def getItem(self): #For take input from user of a object attribute
        x=int(input("Please enter the id: "))
        self.id = x
        y = (input("Enter the name: "))
        self.name = y
        z = int(input("Enter the value of quantity: "))
        self.quantity = z
        w = int(input("Enter the value of cost: "))
        self.cost = w

    def putItem(self): #for print the object attributes
        print("Id: ", self.id)
        print("Name: ", self.name)
        print("Quantity: ", self.quantity)
        print("Cost: ", self.cost)

    def getTotalCost(self): #for calculating the total cost
        if (self.quantity >= 1):
            total=(self.cost * self.quantity)
            return total
        else:
            return 0

    def isEqual(self,obj): #to check two objects are equal
        if self.id == obj.id:
            if self.name == obj.name:
                if self.quantity == obj.quantity:
                    if self.cost == obj.cost:
                        return True
                    else:
                        return False
                else:
                    False
            else:
                False
        else:
            False


    def updateName(self,arr): #update the name on the base of id
        for n in arr:
            if self.id ==n.id:
                n.name= self.name


    def getMinimumCostItem(self,arr): #find minimum cost object
        small=arr[0].cost
        for n in arr:
           if small > n.cost:
               small=n.cost

        for n  in arr:
            if n.cost==small:
                return n


    def getAveragePrice(self,arr): #find the average of the objects cost and assigning to calling objects
        sum=0
        for n in arr:
            sum=sum+n.cost

        avg=sum/3
        self.cost=int(avg)


default=Student()
#ali=Student(1,"ali",1,7)
ali=Student()
zain=Student()
usama=Student()
#ali.setItem(1,"Ali",1,8)
#zain.setItem(1,"Zain",1,4)
#usama.setItem(2,"usama",1,3)
#arr=array([ali,zain,usama])
#ali.updateName(arr,3)
#ali.putItem()
#zain.putItem()
#usama.putItem()
#print(zain.isEqual(ali))
#default=ali.getMinimumCostItem(arr)
#default.putItem()
#ali.getAveragePrice(arr)
ali.putItem()
