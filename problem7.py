a =[]

for i in range (1,11):
    name =input("enter name :")
    age = input("enter age :")
    address = input("enter address :")
    a.append({"name":name,"age":age,"address":address})

for student in a:
    print(student["name"])
 