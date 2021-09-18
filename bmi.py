Height=float(input("enter height in kg: "))
Weight=float(input("enter weight in cm: "))
Weight = Weight/100
BMI = Height/(Weight**2)
print("your Body Mas Index is:", BMI) 
if(BMI<16): 
    print("your are severely underweight")
elif (BMI >= 16 and BMI < 18.5):
    print("you are underweight")
elif(BMI >=18.5 and BMI < 25):
    print("you are Healty")
elif(BMI >= 25 and BMI < 30):
    print("you are overweight")
else: print("you are severely overweight")
