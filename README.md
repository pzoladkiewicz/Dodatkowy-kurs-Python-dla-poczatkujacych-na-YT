[Naucz się Pythona - Pełny kurs dla początkujących | freeCodeCamp.org](https://www.youtube.com/watch?v=rfscVS0vtbw)

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

### Working with numbers
```python
print(2)
print(2.0987)
print(-2.0987)
print(3 + 4.5)              # - + / *
print(3 * 4 + 5)
print(3 * (4 + 5))
print(10 % 3)               # modulo

my_num = 5
print(my_num)
print(str(my_num))          # to string

print(str(my_num) + " is my favourite number")

my_num = -5
print(abs(my_num))

print(pow(3, 2))            # 3^2
print(max(6, 4))            # min
print(round(3.7))

# from math import *
import math as m            
print(m.floor(3.7))
print(m.ceil(3.1))
```

### Getting input from users
```python
name = input("Enter your name: ")
print("Hello " + name + "!" )

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)
```

### Building a basic calculator
```python
num1 = input("Enter a number: ")                # 5
num2 = input("Enter another number: ")          # 8.3
result = num1 + num2                            # 58.3 
print(result)                               

num1 = input("Enter a number: ")                # 5
num2 = input("Enter another number: ")          # 8.3
result = int(num1) + float(num2)                # 13.3 
print(result)
```

### Mad libs game
```python
color = input("Enter a color: ")
plurar_noun = input("Enter a Plurar Noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plurar_noun + " are blue")
print("I love " + celebrity)
```

### Lists
```python
list_example = ["Kevin", 2 , False]     # anything

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)
print(friends[0])                       # Kevin
print(friends[-1])                      # Jim
print(friends[3:])                      # ['Oscar', 'Toby']
print(friends[1:3])                     # ['Karen', 'Jim']

friends[1] = 'Mike'
print(friends[1])                       # Mike
```

### List functions
```python
lucky_numbers = [42, 8, 15, 16, 23]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)                      # ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby']

friends.extend(lucky_numbers)
print(friends)                      # ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42]    

friends.append("Creed")
print(friends)                      # ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42, 'Creed']

friends.insert(1, "Kelly")
print(friends)                      # ['Kevin', 'Kelly', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42, 'Creed']

friends.remove("Jim")
print(friends)                      # ['Kevin', 'Kelly', 'Karen', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42, 'Creed']

friends.pop()                       # last
print(friends)                      # ['Kevin', 'Kelly', 'Karen', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42]

print(friends.index("Kevin"))       # 0         -- index or error
print(friends.count("Toby"))        # 1

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends.sort()                      # not supported between instances of 'int' and 'str'
print(friends)

friends2 = friends.copy()
print(friends2)

friends.clear()
print(friends)                      # []
```

### Tuples
```python
coordinates = (4, 5)                # immutable

coords2 = [(4, 5), (6, 7), (80, 34)]

print(coordinates[1])               # 5
print(coords2[1])                   # (6, 7)

coordinates[1] = 10                 # TypeError: 'tuple' object does not support item assignment
```

