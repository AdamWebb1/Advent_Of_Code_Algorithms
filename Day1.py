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
count = 1

#Iterate through list
for i in range(0, len(depths)-3):
    #Load the window
    window = depths[i:i+3]

    #Convert the window to ints
    for e in range(len(window)):
        window[e] = int(window[e])

    #Check the window
    s = int(sum(window))
    if last < s:
        count += 1
    
    last = s
print(count)
    
