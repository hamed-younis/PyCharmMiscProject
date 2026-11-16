#BMI Calculator

name = input("Enter your name :")
weight = int(input("Enter your weight :"))
height = int(input("Enter your height :"))
BMI = (weight * 703) / (height * height)
print(BMI)

if BMI < 0:
  if(BMI < 18.5):
    print(name +", you are under weight")
  elif(BMI<24.5):
   print(name +", you are a normal weight ")
  elif(BMI<29.5):
   print(name +", you are overweight ")
  elif(BMI<34.5):
   print(name +", you are obese")
  elif(BMI<39.5):
   print(name +", you are serverly obese")
  else:
   print(name +", you are morbidly obese")
else:
  print("Enter a valid input")