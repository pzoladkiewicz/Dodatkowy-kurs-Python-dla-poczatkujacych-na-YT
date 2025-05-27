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
