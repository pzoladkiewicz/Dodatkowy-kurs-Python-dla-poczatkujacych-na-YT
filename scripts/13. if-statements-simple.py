"""
I wake up
If I'm hungry
    I eat breakfast

I leave my house
if it's cloudy
    I bring an umbrella
otherwise
    I bring sunglasses

I'm at a restaurant
if I want meat
    I order a steak
otherwise if I want pasta
    I order spaghetti & meatballs
otherwise
    I order a salad
"""

######################################
is_male = True

if is_male:
    print("You are male")

######################################
is_male = False

if is_male:
    print("You are male")
else:
    print("You are not a male")
    
######################################
is_male = True
is_tall = True

if is_male or is_tall:                          # and, or 
    print("You are male or tall or both")       # True/True, True/False, False/True
else:
    print("You neither male nor tall")          # False/False


######################################
is_male = True
is_tall = False

if is_male and is_tall:                
    print("You are a tall amle")       
elif is_male and not(is_tall):
    print("You are a short male")      
elif not(is_male) and is_tall:
    print("You are not a male but are tall")      
else:
    print("You are not a male and not tall") 
