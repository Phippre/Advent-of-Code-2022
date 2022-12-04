import os

os.chdir("C:/Users/parke/Documents/VS Python/Advent-of-Code-2022/Day1")

elf_tracker = {}
elf_number = 1

part2_solution = 0

with open('data.txt') as f:
    for line in f:
        line = line.strip()
        if line != '':
            try:
                elf_tracker[elf_number] += int(line)
            except:
                elf_tracker[elf_number] = int(line)
        else:
            elf_number += 1

sorted_elfs = sorted(elf_tracker.values())
last_three = list(reversed(sorted_elfs))
last_three = last_three[0:3]
for cal in last_three:
    part2_solution += cal

print(part2_solution)
