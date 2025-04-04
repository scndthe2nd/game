
with open('scratch/0079 - Passcode Derivation/0079_keylog.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file.readlines()]

#Get all occuring digits
digits = set()
for number in numbers:
    digits.update(str(number))

#Initialize dict for keeping digits that are less then key respect in order that they appear
greater_than = { digit:set() for digit in digits}

for number in numbers:
    a,b,c = str(number)
    greater_than[a].add(b)
    greater_than[a].add(c)
    greater_than[b].add(c)


#Order keys by length of set, less elements in a set -> a digit is further from beginning
print(
''.join(map(
    lambda x: x[0], 
    sorted(
        greater_than.items(), 
        key=lambda x: len(x[1]),
        reverse=True,
    )
))
)