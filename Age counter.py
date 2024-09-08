def checkAge(age):
    if age < 0:
        raise ValueError("Only positive integers are allowed")
    if age % 2==0:
        print("Age is even")
    else:
        print("Age is odd")
        
        
try:
        num =int(input("Enter your Age: "))
        checkAge(num)
        
except ValueError:
        print("Only positive numbers are allowed this is outside function")
    