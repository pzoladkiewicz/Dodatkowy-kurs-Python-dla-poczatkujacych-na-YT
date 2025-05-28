number_grid = [1, 2, 3, 5, 7, 9]
    
number_grid2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#print(number_grid2[row][column])
print(number_grid2[1][2])                   # 6
print(number_grid2[3][0])                   # 0
#print(number_grid2[3][1])                   # IndexError: list index out of range


# nested for loop
for row in number_grid2:
    print(row)
"""
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
[0]
"""
    

for row in number_grid2:
    for col in row:
        print(col)  
"""
1
2
3
4
5
6
7
8
9
0
"""   
