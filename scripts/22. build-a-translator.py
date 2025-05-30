"""
Giraffe Language
vowels -> g
-----------------
dog -> dgg
cat -> cgt
"""

def translate(phrase):
    transalation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                transalation = transalation + "G"
            else:
                transalation = transalation + "g"
        else:
            transalation = transalation + letter
    return transalation
    
print(translate(input("Enter a phrase: ")))

# To be or not to be => Tg bg gr ngt tg bg
