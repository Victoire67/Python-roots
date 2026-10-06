class Employee:
    def __init__(self , name , age , salary , sex):
        self.name = name 
        self.age = age 
        self.salary = salary
        self.sex = sex
        pass

    def greet(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old")



victoire = Employee('Victoire', 23 , 600000 , 'M')

victoire.greet()


# self parameter : every method in python should have the self as it's first parameter , and this will be applied to all of the rest of elements

# Magic methods 

class Student:
    def __init__(self , name , age , school):
        self.name = name 
        self.age = age
        self.school = school

    def __str__(self):
        print(f"Student : {self.name}")
        return 'displayed'



me = Student('Victor' , 12 , 'Antonino')


print(me)