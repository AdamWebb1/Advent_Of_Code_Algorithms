
x = 0
y = 0
aim = 0

'''
with open("input.txt", "r") as f:
    directions = f.read().splitlines()

def whatType(inp):
    return inp[0], int(inp[-1])

for direction in directions:
    directionType = whatType(direction)
    if directionType[0] == "f":
        x += directionType[1]
    
    elif directionType[0] == "d":
        y += directionType[1]

    elif directionType[0] == "u":
        y -= directionType[1]

    else:
        raise ValueError(f"Value of {directionType} was not expected")

print(x, y, x*y)

x, y = 0, 0
'''

with open("input.txt", "r") as f:
    directions = f.read().splitlines()

def whatType(inp):
    return inp[0], float(inp[-1])

for direction in directions:
    directionType = whatType(direction)
    if directionType[0] == "f":
        x += directionType[1]
        y += aim*directionType[1]
    
    elif directionType[0] == "d":
        aim += directionType[1]

    elif directionType[0] == "u":
        aim -= directionType[1]

    else:
        raise ValueError(f"Value of {directionType} was not expected")

    print(x, y, aim)

print(x, y, x*y)