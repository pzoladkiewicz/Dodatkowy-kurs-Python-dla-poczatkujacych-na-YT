def cube(num):
    num*num*num

print(cube(3))              # None

###########################################################
def cube(num):
    return num*num*num    

print(cube(3))              # 27
print(cube(4))              # 64

###########################################################
def cube(num):
    return num*num*num
    print("code")           # not returning

result = cube(4)
print(result)               # 64
