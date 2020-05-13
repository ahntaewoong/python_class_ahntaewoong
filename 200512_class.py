class Athlete:
    def __init__(self, value = 'Jane'):
        self.thing = value
    def getAthlete(self):
        return self.thing
a = Athlete()
print(a.getAthlete())
b = Athlete('Holy')
Athlete.__init__(a, 'Holy')
print(b.getAthlete())

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def innerPrint(self, infor):
        print(infor, self.x, self.y)

pt1 = Point()
print('Point01 class', pt1.x, ',', pt1.y)
pt2 = Point(3,5)
print('Point02 class', pt2.x, ',', pt2.y)
pt2.innerPrint('Point02 InnerPrint : ')

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def displayEmployee(self):
        print('Name : ',self.name, ', Salary : ', self.salary)

emp1 = Employee('Zara', 2000)
emp1.displayEmployee()
emp2 = Employee('Manni', 5000)
emp2.displayEmployee()

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def displayEmployee(self, name, dailywage, weekly):
        self.name = name
        self.dailywage = dailywage
        self.weekly = weekly
        return print('name : {}, salary : {}'.format(self.name, self.dailywage*self.weekly))

emp1 = Employee("Zara",200)
emp1.displayEmployee("Zara",200,5)