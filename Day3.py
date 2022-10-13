gamma = 0
count0 = 0
count1 = 0

def BinaryToDecimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal

gamma = ""

with open("input.txt", "r") as f:
    diagnostics = f.read().splitlines()

for i in range(len(diagnostics[0])):
    for diagnostic in diagnostics:
        if diagnostic[i] == "0": count0 += 1
        elif diagnostic[i] == "1": count1 += 1
    
    print(count0, count1)
    if count0 > count1:
        gamma += "0"
    elif count1 > count0:
        gamma += "1"
    
    count0, count1 = 0, 0

epsilon = "".join('1' if x == '0' else '0' for x in gamma)
print(gamma, epsilon)

gamma = BinaryToDecimal(gamma)
epsilon = BinaryToDecimal(epsilon)

print(gamma, epsilon, gamma*epsilon)