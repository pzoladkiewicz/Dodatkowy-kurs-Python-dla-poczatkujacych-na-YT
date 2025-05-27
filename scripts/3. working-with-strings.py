print("Giraffe Academy")
print("Giraffe\nAcademy")       # escape char
print("Giraffe\"Academy")
print("Giraffe\Academy")

phrase = "Giraffe Academy"
print(phrase)

print(phrase + " is cool")      # concatenation

print(phrase.lower())           # functions 
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())

print(len(phrase))              # length: 15

phrase = "Giraffe Academy"
# [index] 0123..
print(phrase[0])                # letter at [index]: G

print(phrase.index("r"))        # index of "G": 0
print(phrase.index("Acad"))     # 8

print(phrase.replace("Giraffe", "Elephant"))
