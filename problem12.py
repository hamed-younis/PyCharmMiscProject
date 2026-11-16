class Person:
        
      name = ""
      age = ""
      address = ""
      email = ""

      def input_data(self):
      
        self.name = input("enter your name: ")
        self.age = input("enter your age: ")
        self.address = input("enter your address: ")
        self.email = input("enter your email: ")

class Student(Person):
      
      def __init__(self):
            
            self.input_data()
            self.class_name = input("enter your class name: ")
            self.roll_num = input("enter your roll number: ")
            self.print_data1()

      def print_data1(self):
            
            print(self.name)
            print(self.age)
            print(self.address)
            print(self.email)
            print(self.class_name)
            print(self.roll_num)

class Teacher(Person):
      
      def __init__(self):
                        
                        
            self.input_data()
            self.employee_id = input("enter your employee id: ")
            self.monthly_intake = input("enter your salary: ")
            self.print_data2()


      def print_data2(self):
      
          print(self.name)
          print(self.age)
          print(self.address)
          print(self.email)
          print(self.employee_id)
          print(self.monthly_intake)



s1 = Student()
t1 = Teacher()
