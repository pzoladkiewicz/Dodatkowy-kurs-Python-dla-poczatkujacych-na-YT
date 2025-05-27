coordinates = (4, 5)                # immutable

coords2 = [(4, 5), (6, 7), (80, 34)]

print(coordinates[1])               # 5
print(coords2[1])                   # (6, 7)

coordinates[1] = 10                 # TypeError: 'tuple' object does not support item assignment
