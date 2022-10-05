class Employee:
    no_of_leaves = 10

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printdetails(self):
                print("Employee ",self.name,"has ", self.no_of_leaves," leaves his age is ",self.age)
    # emp1=Employee(readlines())
    
file = open('exercise.txt', "r")
content = file.readlines()

employees = []
i =0
emp = [0,0,0]
for line in content:
    name, age = line.strip().split(',')

    # employees.append({'name': name, 'age': int(age)})
    emp[i] = Employee(name,age)
    emp[i].printdetails()
    i+=1

# print(employees)

file.close()