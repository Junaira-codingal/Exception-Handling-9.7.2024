valid = False

while not valid:
    
    try:
        n = int(input("Enter a number: "))
        
        if n%2 == 0:
            print("Bye BYE")
            valid = True
            
    
    except ValueError:
        print("Invalid Data Type")