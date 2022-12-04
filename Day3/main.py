import os
os.chdir("C:/Users/parke/Documents/VS Python/Advent-of-Code-2022/Day3")

priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
pri_total = 0
all_rucks_primary = []
#all_rucks_secondary = []
matches = []

with open('data.txt') as f:
    for line in f:
        all_rucks_primary.append(line.strip())

def slice_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

sliced = list(slice_list(all_rucks_primary, 3))

for i in range(len(sliced)):
    first_ruck = sliced[i][0]
    second_ruck = sliced[i][1]
    third_ruck = sliced[i][2]
    for x in range(len(first_ruck)):
        if second_ruck.__contains__(first_ruck[x]) and third_ruck.__contains__(first_ruck[x]):
            matches.append(first_ruck[x])
            break

for i in range(len(matches)):
    for j in range(len(priority)):
        if matches[i] == priority[j]:
            pri_total += j + 1

print(pri_total)

#with open('data.txt') as f:
#    for line in f:
#        ruck_size = len(line.strip()) / 2
#        all_rucks_primary.append(line.strip()[0:int(ruck_size)])
#        all_rucks_secondary.append(line.strip()[int(ruck_size):])
#
#
#for x in range(len(all_rucks_primary)):
#    for y in range(len(all_rucks_primary[x])):
#        if all_rucks_secondary[x].__contains__(all_rucks_primary[x][y]):
#            matches.append(all_rucks_primary[x][y])
#            break
#
#for i in range(len(matches)):
#    for j in range(len(priority)):
#        if matches[i] == priority[j]:
#            pri_total += j + 1
#
#print(pri_total)