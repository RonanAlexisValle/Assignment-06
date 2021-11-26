def user_input():
    num1=float(input("Enter the First number: "))
    num2=float(input("Enter the Second number: "))
    num3=float(input("Enter the Third number: "))
    num4=float(input("Enter the Fourth number: "))
    return num1,num2,num3,num4

num1,num2,num3,num4 = user_input()

def sorter():
    if num1 > num2 and num2 > num3 and num3 > num4:
        print(f"Descending Order: {num1,num2,num3,num4}")
        if num1 > num2 and num2 > num4 and num4 > num3:
            print(f"Descending Order: {num1,num2,num4,num3}")
            if num1 > num3 and num3 > num4 and num4 > num2:
                print(f"Descending Order: {num1,num3,num4,num2}")
                if num1 > num3 and num3 > num2 and num2 > num4:
                    print(f"Descending Order: {num1,num3,num2,num4}")
        if num1 > num4 and num4 > num2 and num2 > num3:
                        print(f"Descending Order: {num1,num4,num2,num3}")
        else:
                        print(f"Descending Order: {num1,num4,num3,num2}")

    elif num2 > num1 and num1 > num3 and num3 > num4:
        print(f"Descending Order: {num2,num1,num3,num4}")
        if num2 > num1 and num1 > num4 and num4 > num3:
            print(f"Descending Order: {num2,num1,num4,num3}")
            if num2 > num3 and num3 > num4 and num4 > num1:
                print(f"Descending Order: {num2,num3,num4,num1}")
                if num2 > num3 and num3 > num1 and num1 > num4:
                    print(f"Descending Order: {num2,num3,num1,num4}")
        if num2 > num4 and num4 > num3 and num3 > num1:
                        print(f"Descending Order: {num2,num4,num3,num1}")
        else:
                        print(f"Descending Order: {num2,num4,num1,num3}")

    elif num3 > num1 and num1 > num2 and num2 > num4:
        print(f"Descending Order: {num3,num1,num2,num4}")
        if num3 > num1 and num1 > num4 and num4 > num2:
            print(f"Descending Order: {num3,num1,num4,num2}")
            if num3 > num2 and num2 > num4 and num4 > num1:
                print(f"Descending Order: {num3,num2,num4,num1}")
                if num3 > num2 and num2 > num1 and num1 > num4:
                    print(f"Descending Order: {num3,num2,num1,num4}")
        if num3 > num4 and num4 > num1 and num1 > num2:
                        print(f"Descending Order: {num3,num4,num1,num2}")
        else:
                        print(f"Descending Order: {num3,num4,num2,num1}")

    elif num4 > num1 and num1 > num2 and num2 > num3:
        print(f"Descending Order: {num4,num1,num2,num3}")
        if num4 > num1 and num1 > num3 and num3 > num2:
            print(f"Descending Order: {num4,num1,num3,num2}")
            if num4 > num2 and num2 > num1 and num1 > num3:
                print(f"Descending Order: {num4,num2,num1,num3}")
                if num4 > num2 and num2 > num3 and num3 > num1:
                    print(f"Descending Order: {num4,num2,num3,num1}")
        if num4 > num3 and num3 > num1 and num1 > num2:
                        print(f"Descending Order: {num4,num3,num1,num2}")
        else:
                        print(f"Descending Order: {num4,num3,num2,num1}")

sorter()
    
   