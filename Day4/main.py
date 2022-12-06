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
        overlaps2.append(x.split('-'))


for i in range(0, len(overlaps2), 2):
    try:
        if overlaps2[i][0] > overlaps2[i + 1][0] and overlaps2[i][0] < overlaps2[i + 1][1] and overlaps2[i][1] > overlaps2[i + 1][0] and overlaps[i][1] < overlaps[i + 1][1]:
            #print('First range is within the second')
            counter += 1
        elif overlaps2[i + 1][0] > overlaps2[i][0] and overlaps2[i + 1][0] < overlaps2[i][1] and overlaps2[i + 1][1] > overlaps2[i][0] and overlaps2[i + 1][1] < overlaps2[i][1]:
            #print('Second range is within the first')
            counter += 1
    except:
        print("Stopped at index: ", i)
        print(sys.exc_info()[0])

