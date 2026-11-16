class Student:

    def __init__(self):
         self.name=input("enter your name")
         self.age = input("enter your age")
         self.address= input("enter your adress")
         self.subject = input("enter your subject name")
         self.phone = input("Enter your number")
         self.print_data()
    
    def print_data(self):
         print(self.name)
         print(self.age)
         print(self.address)
         print(self.subject)
         print(self.phone)
         

s1 = Student()
s2 = Student()
