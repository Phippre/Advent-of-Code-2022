import os

os.chdir('C:/Users/parke/Documents/VS Python/Advent-of-Code-2022/Day6')

data_stream = []

with open('data.txt') as f:
    for line in f:
        data_stream.append(line.strip())


def check_set(arr):
    for letter in range(len(arr)):
        spot = letter
        test_letter = arr.pop(letter)
        if arr.__contains__(test_letter):
            arr.insert(spot, test_letter)
            return True
        else:
            arr.insert(spot, test_letter)
    return False

for letter in range(len(data_stream[0])):
    letter_range = [data_stream[0][x] for x in range(letter, letter + 14)]
    if check_set(letter_range) == False:
        print('Found set with no matching pairs!', letter + 14, letter_range)
        break
    elif check_set(letter_range) == True:
        print(letter_range, letter)
    