# gamma = 0
# count0 = 0
# count1 = 0





def BinaryToDecimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal

# gamma = ""


with open("input.txt", "r") as f:
    diagnostics = f.read().splitlines()

cache = diagnostics

# for i in range(len(diagnostics[0])):
#     for diagnostic in diagnostics:
#         if diagnostic[i] == "0": count0 += 1
#         elif diagnostic[i] == "1": count1 += 1
    
#     print(count0, count1)
#     if count0 > count1:
#         gamma += "0"
#     elif count1 > count0:
#         gamma += "1"
    
#     count0, count1 = 0, 0

# epsilon = "".join('1' if x == '0' else '0' for x in gamma)
# print(gamma, epsilon)

# gamma = BinaryToDecimal(gamma)
# epsilon = BinaryToDecimal(epsilon)

# print(gamma, epsilon, gamma*epsilon)

def countOnes(col, data):
    count = 0
    for diagnostic in data:
        if diagnostic[col] == "1": count += 1
    return count

def countZeros(col, data):
    count = 0
    for diagnostic in data:
        if diagnostic[col] == "0": count += 1
    return count

def getOpposite(inp):
    return "1" if inp == "0" else "1"

def getMostCommon(ones, zeros, bias):
    if ones > zeros:
        return 1
    elif ones < zeros:
        return 0
    return bias

# Oxygen Generator

#FOR EVERY BIT
  #If the length of the diagnostics is NOT 1
    #Find most common value

    #Delete most common value

for bit in range(len(diagnostics[0])):
    nOnes = countOnes(bit, diagnostics)
    nZeros = countZeros(bit, diagnostics)

    mostCommon = getMostCommon(nOnes, nZeros, 1)

    for value in range(len(diagnostics)-1, -1, -1):
        if int(diagnostics[value][bit]) != mostCommon:
            if len(diagnostics) == 1:
                print("done")
                break
            print("popped: " + str(diagnostics.pop(value)))

oxygen = diagnostics[0]

#reread input file
with open("input.txt", "r") as f:
    diagnostics = f.read().splitlines()

print(diagnostics)

for bit in range(len(diagnostics[0])):
    nOnes = countOnes(bit, diagnostics)
    nZeros = countZeros(bit, diagnostics)

    mostCommon = getMostCommon(nOnes, nZeros, 0)

    for value in range(len(diagnostics)-1, -1, -1):
        if int(diagnostics[value][bit]) == mostCommon:
            if len(diagnostics) == 2:
                print(diagnostics)
                print(diagnostics[value], diagnostics[value][bit], bit)
            if len(diagnostics) == 1:
                print("done")
                break
            print("popped: " + str(diagnostics.pop(value)))

print(diagnostics)
co2 = diagnostics[0]

print(nOnes, nZeros, mostCommon)

print(oxygen, co2, BinaryToDecimal(oxygen), BinaryToDecimal(co2),  BinaryToDecimal(oxygen) * BinaryToDecimal(co2))














# print(oxygen, CO2, BinaryToDecimal(oxygen)*BinaryToDecimal(CO2))