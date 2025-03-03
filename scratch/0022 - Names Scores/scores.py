#a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3+15+12+9+14 = 53 is the 938th name on the list, so it would score 938x53 = 49714.

#What is the total score of all the names stored in this file?

def read_from_file(filename):
    with open(filename, 'r') as file:
        items = file.read()
    return items

raw = read_from_file("scratch/0022 - Names Scores/0022_names.txt")
split = raw.split(",")
sorted_names = sorted(split,reverse=False)
number_of_names = len(sorted_names)


total = 0

for index_number, name in enumerate(sorted_names, start=1):
    name_value = 0
    for letter in name:
        if letter == '"':
            continue
        letter_value = ord(letter.upper()) - ord('A') + 1
        name_value += letter_value
    name_value *= index_number
    total += name_value
    print(f"index = {index_number}, name = {name}, name_value = {name_value}, total = {total}")   