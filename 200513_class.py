class Employee:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print("Total Employee", Employee.empCount)
    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print("Total Employee", Employee.empCount)

class NamedList(list):
    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name
        self.dob = None
johnny = NamedList('John Paul Jones')
normelvar = 3

johnny.dob = '2017.10.10'
johnny.extend(['Composer', 'Arranger', 'Musician'])

for attr in johnny:
    print(johnny.name + ' is a '+ attr + '.-' + johnny.dob)



import pickle
favorite_color = {'lion' : 'yellow', 'kitty' : 'red'}
pickle.dump(favorite_color, open('save.pkl', 'wb'))
favorite_color_load = pickle.load(open('save.pkl', 'rb'))
print(favorite_color_load)

from ClassEmployee import Employee as emp
emp1 = emp('Zara', 2000)
emp1.displayEmployee()

import pickle
pickle.dump(emp1,open("./emp1.pkl", "wb"))
print('dump pickle')
emp1_pkl = pickle.load(open("./emp1.pkl", "rb"))
print('load pickle')
emp1_pkl.displayEmployee()