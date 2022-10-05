

with open("input.txt", "r") as f:
    depths = f.read().splitlines()

count = 0
last = None

# for depth in depths:
#     if last == None:
#         pass

#     elif last < depth:
#         count += 1
    
#     last = depth

window = []

for depth in depths:
    
    if len(window) == 2:
        window.pop(0)
    window.append(int(depth))
    print(window)

    depthSum = sum(window)
    print(depthSum)
    if last == None:
        pass
    elif last < depthSum:
        count += 1 
        print("YES")

    last = depthSum
    

print(count)