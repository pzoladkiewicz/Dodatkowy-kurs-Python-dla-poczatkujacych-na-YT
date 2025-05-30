try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")
    
#####################################

try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")                      # it's not Invalid Input should be div/0 error
    
####################################

try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero!")
except ValueError:
    print("Invalid Input") 
    
####################################

try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
