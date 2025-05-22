### Hello World
```python
print("Hello World!")
```
### Drawing a Shape
```python
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
```
### Variables & Data Types
```python
print("There once was a man named George, ")
print("he was 70 years old. ")
print("He really liked the name George, ")
print("but didn't like being 70.")
```
```python
character_name = "John"
character_age = "35"
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")
```
```python
character_name = "John"
character_age = "35"
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")

character_name = "Mike"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")
```
```python
character_name = "John"         # string
character_age = 35              # number
is_male = True                  # boolean
print("There once was a man named " + character_name + ", ")
print("he was " + str(character_age) + " years old. ")
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + str(character_age) + ".")
```
### Working with strings
```python
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
```
