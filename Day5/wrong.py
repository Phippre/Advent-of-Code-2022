import os
import sys
os.chdir('C:/Users/parke/Documents/VS Python/Advent-of-Code-2022/Day5')
#            [Q]     [G]     [M]    
#            [B] [S] [V]     [P] [R]
#    [T]     [C] [F] [L]     [V] [N]
#[Q] [P]     [H] [N] [S]     [W] [C]
#[F] [G] [B] [J] [B] [N]     [Z] [L]
#[L] [Q] [Q] [Z] [M] [Q] [F] [G] [D]
#[S] [Z] [M] [G] [H] [C] [C] [H] [Z]
#[R] [N] [S] [T] [P] [P] [W] [Q] [G]
# 1   2   3   4   5   6   7   8   9 

stacks = [['R', 'S', 'L', 'F', 'Q'],
          ['N', 'Z', 'Q', 'G', 'P', 'T'],
          ['S', 'M', 'Q', 'B'],
          ['T', 'G', 'Z', 'J', 'H', 'C', 'B', 'Q'],
          ['P', 'H', 'M', 'B', 'N', 'F', 'S'],
          ['P', 'C', 'Q', 'N', 'S', 'L', 'V', 'G'],
          ['W', 'C', 'F'],
          ['Q', 'H', 'G', 'Z', 'W', 'V', 'P', 'M'],
          ['G', 'Z', 'D', 'L', 'C', 'N', 'R']
         ]

instructions = []

with open('data.txt') as f:
    for line in f:
        temp = []
        temp.append(line.strip().split(' '))
        for char in temp[0]:
            if char.isdigit():
                instructions.append(int(char))
                

for inst in range(0, len(instructions), 3):
    how_many = instructions[inst]
    trips_by_3 = int(how_many / 3)
    left_over = how_many % 3
    destination = stacks[instructions[inst + 2] - 1]
    print('Instructions Sent | Amount:', how_many, "Source:", stacks[instructions[inst + 1] - 1], 'Destination:', destination, 'Trips by 3:', trips_by_3, 'Remainder:', left_over)
    if how_many >= 3 and trips_by_3 > 0:
        for i in range(trips_by_3):
            print("Making trip with 3")
            stuff_to_move = stacks[instructions[inst + 1] - 1][-3:]
            del stacks[instructions[inst + 1] - 1][-3:]
            for item in stuff_to_move:
                destination.append(item)
            trips_by_3 -= 1
    
    if left_over > 0 and trips_by_3 == 0:
        print('Making left over trip with', left_over)
        left_to_move = stacks[instructions[inst + 1] - 1][-left_over:]
        del stacks[instructions[inst + 1] - 1][-left_over:]
        for item in left_to_move:
            destination.append(item)

print(stacks)
    
#for i in range(instructions[inst]):
#   stacks[instructions[inst + 2] - 1].append(stacks[instructions[inst + 1] - 1].pop())
