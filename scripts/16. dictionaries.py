montyhConversions = {
     "Jan": "January"
    ,"Feb": "February"
    ,"Mar": "March"
    ,"Apr": "April"
    ,"May": "May"
    ,"Jun": "June"
    ,"Jul": "July"
    ,"Aug": "August"
    ,"Sep": "September"
    ,"Oct": "October"
    ,"Nov": "November"
    ,"Dec": "December"
    }
    
print(montyhConversions["Nov"])                             #   November
print(montyhConversions.get("Nov"))                         #   November
print(montyhConversions.get("Luv"))                         #   None
print(montyhConversions.get("Luv", "Not a valid Key"))      #   Not a valid Key

"""
montyhConversions = {
     1: "January"
    ,2: "February"
    ,3: "March"
    .
    .
    .
    ,11: "November"
    ,12: "December"
    }
"""
