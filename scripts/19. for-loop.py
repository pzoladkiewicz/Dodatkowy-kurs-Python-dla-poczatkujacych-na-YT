for lr in "Giraffe Academy":
    print(lr)
    

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)
    
for index in range(10):                     
    print(index)                            # 0...9
    
for index in range(3, 10):
    print(index)                            # 3...9
    
friends = ["Jim", "Karen", "Kevin"]
for index in range(len(friends)):
    print(friends[index])                   ## Jim, Karen, Kevin
    
for index in range(5):
    if index == 0:
        print("First iteration")
    else:                     
        print("Iteration #" + str(index))    
