def calculate(weight,height):
    bmi=weight/(height ** 2)
    if(bmi<0):
        print("Invalid inputs. ")
    elif(bmi<18.5):
        print("Under Weight")
    elif(bmi<=24.9):
        print("Normal")
    elif(bmi<=29.9):
        print("Over Weight")
    else:
        print("Person has obesity.")
wt=float(input("Enter the weight in kgs : "))
ht=float(input("enter height in meters : "))
calculate(wt,ht)
