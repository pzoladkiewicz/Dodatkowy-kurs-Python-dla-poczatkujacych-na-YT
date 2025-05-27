def say_hi():
    print("Hello User")    
say_hi()                        # Hello User


# parameters
def say_hi(name, age):
    print("Hello " + name + ", you are " + age)
say_hi("Mike", "35")
say_hi("Steve", "70")


def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))
say_hi("Mike", 35)
say_hi("Steve", 70)
