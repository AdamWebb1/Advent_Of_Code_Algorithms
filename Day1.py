import sys

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
last = sys.maxsize - 1
count = 0

#Iterate through list
for i in range(0, len(depths)-3):
    #Load the window
    window = depths[i:i+3]

    #Convert the window to ints
    for e in range(len(window)-1):
        window[e] = int(window[e])

    #Check the window
    if last < sum(window):
        count += 1
print(count)

"""
for depth in depths:
    
    if len(window) == 2:
        window.pop(0)
    window.append(int(depth))
    # print(window)

    depthSum = sum(window)
    print(depthSum)
    if last == None:
        pass
    elif last < depthSum:
        count += 1 
        print("YES")

    last = depthSum

"""

#
    
