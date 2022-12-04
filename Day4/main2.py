import os
import sys

os.chdir("C:/Users/parke/Documents/VS Python/Advent-of-Code-2022/Day4")

overlaps = []
overlaps2 = []
counter = 0

with open('data.txt') as f:
    for line in f:
        overlaps.append(line.strip())

for i in overlaps:
    test = i.split(',')
    for x in test:
        next = x.split('-')
        next[0] = int(next[0])
        next[1] = int(next[1])
        overlaps2.append(next)
        
for i in range(0, len(overlaps2), 2):
    if overlaps2[i][0] >= overlaps2[i + 1][0] and overlaps2[i][0] <= overlaps2[i + 1][1] and overlaps2[i][1] >= overlaps2[i + 1][0] and overlaps2[i][1] <= overlaps2[i + 1][1]:
        print('First Statement Passed!  |  Current index: ', i, '  |  Comparing Values: ', overlaps2[i], overlaps2[i + 1])
        counter += 1
    elif overlaps2[i + 1][0] >= overlaps2[i][0] and overlaps2[i + 1][0] <= overlaps2[i][1] and overlaps2[i + 1][1] >= overlaps2[i][0] and overlaps2[i + 1][1] <= overlaps2[i][1]:
        print('Second Statement Passed!  |  Current index: ', i, '  |  Comparing Values: ', overlaps2[i], overlaps2[i + 1])
        counter += 1
    elif overlaps2[i][0] <= overlaps2[i + 1][0] and overlaps2[i][1] >= overlaps2[i + 1][0] and overlaps2[i][1] <= overlaps2[i + 1][1]:
        print('Third Statement Passed!  |  Current index: ', i, '  |  Comparing Values: ', overlaps2[i], overlaps2[i + 1])
        counter += 1
    elif overlaps2[i + 1][0] >= overlaps2[i][0] and overlaps2[i + 1][0] <= overlaps2[i][1] and overlaps2[i + 1][1] >= overlaps2[i][1]:
        print('Fourth Statement Passed!  |  Current index: ', i, '  |  Comparing Values: ', overlaps2[i], overlaps2[i + 1])
        counter += 1
    elif overlaps2[i][0] >= overlaps2[i + 1][0] and overlaps2[i][0] <= overlaps2[i + 1][1]:
        print('Fifth Statement Passed!  |  Current index: ', i, '  |  Comparing Values: ', overlaps2[i], overlaps2[i + 1])
        counter += 1
    else:
        print("No overlaps at index: ", i, '  |  Compared Values: ', overlaps2[i], overlaps2[i + 1])

print(counter)