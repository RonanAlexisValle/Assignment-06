#This program will sort four random numbers inputted by the user in descending order
#This program used "if","elif" and "else" statements

#STEP.1--The program will ask the user to input 4 random numbers.(Can be an int or a float)
def user_input():
    num1=float(input("Enter the First number: "))
    num2=float(input("Enter the Second number: "))
    num3=float(input("Enter the Third number: "))
    num4=float(input("Enter the Fourth number: "))
    return num1,num2,num3,num4

num1,num2,num3,num4 = user_input()

#STEP.2--In this step, the inputted numbers will be sorted according to the given conditions below.
#        Then it will display the sorted numbers on the output screen.
def Descending_Sorter():
    
    #Conditionn if the first number is the highest
    if num1 > num2 and num2 > num3 and num3 > num4:
        print(f"Descending Order: {num1,num2,num3,num4}")
    elif num1 > num2 and num2 > num4 and num4 > num3:
        print(f"Descending Order: {num1,num2,num4,num3}")
    elif num1 > num3 and num3 > num4 and num4 > num2:
        print(f"Descending Order: {num1,num3,num4,num2}")
    elif num1 > num3 and num3 > num2 and num2 > num4:
        print(f"Descending Order: {num1,num3,num2,num4}")
    elif num1 > num4 and num4 > num2 and num2 > num3:
        print(f"Descending Order: {num1,num4,num2,num3}")
    elif num1 > num4 and num4 > num2 and num2 > num3:
        print(f"Descending Order: {num1,num4,num3,num2}")

    #Conditionn if the second number is the highest
    elif num2 > num1 and num1 > num3 and num3 > num4:
        print(f"Descending Order: {num2,num1,num3,num4}")
    elif num2 > num1 and num1 > num4 and num4 > num3:
        print(f"Descending Order: {num2,num1,num4,num3}")
    elif num2 > num3 and num3 > num4 and num4 > num1:
        print(f"Descending Order: {num2,num3,num4,num1}")
    elif num2 > num3 and num3 > num1 and num1 > num4:
        print(f"Descending Order: {num2,num3,num1,num4}")
    elif num2 > num4 and num4 > num3 and num3 > num1:
        print(f"Descending Order: {num2,num4,num3,num1}")
    elif num2 > num4 and num4 > num1 and num1 > num3:
        print(f"Descending Order: {num2,num4,num1,num3}")

    #Conditionn if the third number is the highest
    elif num3 > num1 and num1 > num2 and num2 > num4:
        print(f"Descending Order: {num3,num1,num2,num4}")
    elif num3 > num1 and num1 > num4 and num4 > num2:
        print(f"Descending Order: {num3,num1,num4,num2}")
    elif num3 > num2 and num2 > num4 and num4 > num1:
        print(f"Descending Order: {num3,num2,num4,num1}")
    elif num3 > num2 and num2 > num1 and num1 > num4:
        print(f"Descending Order: {num3,num2,num1,num4}")
    elif num3 > num4 and num4 > num1 and num1 > num2:
        print(f"Descending Order: {num3,num4,num1,num2}")
    elif num3 > num4 and num4 > num2 and num2 > num1:
        print(f"Descending Order: {num3,num4,num2,num1}")

    #Conditionn if the fourth number is the highest
    elif num4 > num1 and num1 > num2 and num2 > num3:
        print(f"Descending Order: {num4,num1,num2,num3}")
    elif num4 > num1 and num1 > num3 and num3 > num2:
        print(f"Descending Order: {num4,num1,num3,num2}")
    elif num4 > num2 and num2 > num1 and num1 > num3:
        print(f"Descending Order: {num4,num2,num1,num3}")
    elif num4 > num2 and num2 > num3 and num3 > num1:
        print(f"Descending Order: {num4,num2,num3,num1}")
    elif num4 > num3 and num3 > num1 and num1 > num2:
        print(f"Descending Order: {num4,num3,num1,num2}")

    else:
        print(f"Descending Order: {num4,num3,num2,num1}")

Descending_Sorter()
    


    
   
