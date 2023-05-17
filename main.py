#make a vehicle class
class Vehicle:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def getMake(self):
    return self.make
  def getModel(self):
    return self.model

class Car(Vehicle):
  def __init__(self, make, model, doorNum):
    Vehicle.__init__(self, make, model)
    self.doorNum = doorNum
  def doorNum(self):
    return self.doorNum
# define print details car
  def printDetails(self):
    print("car Make :", self.make)
    print("car Model :", self.model)
    print("car Number of Doors", self.doorNum)

#define truck
class Truck(Vehicle):
  def __init__(self, make, model, bedLength):
    Vehicle.__init__(self, make, model)
    self.bedLength = bedLength
  def bedLength(self):
    return self.bedLength
#define print details for truck
  def printDetails(self):
    print("truck Make :",self.make)
    print("truck Model :", self.model)
    print("truck Bed Length :", self.bedLength)

garage=[]
while(True):
  option = int(input("Enter \n1 for Car \n2 for Truck \n3 for exit \n"))
  if(option==1):
    make=input("Enter car make :")
    model=input("Enter car model :")
    doorNum=int(input("Enter Number of Doors :"))
    p=Car(make, model, doorNum)
    garage.append(p)
  elif(option==2):
    make=input("Enter Truck Make :")
    model=input("Enter Truck Model :")
    bedLength=int(input("Enter Truck bed Length :"))
    t=Truck(make, model, bedLength)
    garage.append(t)
  else:
    break

print("Vehicles Details is :")
print("-------------------------")
for a in garage:
  print(a.printDetails())

  
  