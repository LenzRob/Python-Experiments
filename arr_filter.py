import random
#Choose Static (True) or Random (False) Array switch Boolean for it :)
choose = True

#Test Case Static
numbers_static = [0, 0, 1, 2, 3, 0, 1, 1]

#Test Case Random (Change randint values for different ranges)
numbers_random = []
for i in range(random.randint(0,20)):
    numbers_random.append(random.randint(0,20))

#Pick Choosen Array
numbers = []
if choose == True:
    numbers = numbers_static
else:
    numbers = numbers_random

#Berechene Individuele vorkommende Nummern
found_numbers = []
for i in range(len(numbers)):
    number_includes = False
    for j in range(len(found_numbers)):
        if numbers[i] == found_numbers[j]:
            number_includes = True
    if number_includes == False:
        found_numbers.append(numbers[i])

#Berechne insgesamt vorkommende Nummbern
total_numbers = [0] * len(found_numbers)
for i in range(len(numbers)):
    indexOfFoundNumber = found_numbers.index(numbers[i])
    total_numbers[indexOfFoundNumber] += 1

#Fertige Array mit den Meisten vorkommenen Numbers an
maxTotalNumbers = 0
for i in range(len(total_numbers)):
    maxTotalNumbers = max(maxTotalNumbers, total_numbers[i])
max_numbers = []
for i in range(len(total_numbers)):
    if maxTotalNumbers == total_numbers[i]:
        for j in range(maxTotalNumbers):
            max_numbers.append(found_numbers[i])

#Result and Debug Outputs
print(numbers, "<- Input Array")
print(found_numbers, "<- Output Array of individual Found Numbers")
print(total_numbers, "<- Total Numbers found")
print(maxTotalNumbers, "<- Highest Found Numbers in Total")
print(max_numbers, "<- Final Array with only max found numbers")
