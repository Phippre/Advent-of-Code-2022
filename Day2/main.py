import os
os.chdir("C:/Users/parke/Documents/VS Python/Advent-of-Code-2022/Day2")

#A = Rock = X
#B = Paper = Y
#C = Scissors = Z

#1 Point for Rock, 2 Points for Paper and 3 Points for Scissors
#0 Points if you lose, 3 Points for Draw, 6 Points for winning

score = 0
score_part_two = 0
all_rounds = []

with open('data.txt') as f:
    for line in f:
        line = line.strip()
        all_rounds.append(line.split(' '))

#print(all_rounds)

for game in all_rounds:
    if game[0] == "A" and game[1] == "X":
        score += 4
        score_part_two += 3
    elif game[0] == "A" and game[1] == "Y":
        score += 8
        score_part_two += 4
    elif game[0] == "A" and game[1] == "Z":
        score += 3
        score_part_two += 8
    elif game[0] == "B" and game[1] == "X":
        score += 1
        score_part_two += 1
    elif game[0] == "B" and game[1] == "Y":
        score += 5
        score_part_two += 5
    elif game[0] == "B" and game[1] == "Z":
        score += 9
        score_part_two += 9
    elif game[0] == "C" and game[1] == "X":
        score += 7
        score_part_two += 2
    elif game[0] == "C" and game[1] == "Y":
        score += 2
        score_part_two += 6
    elif game[0] == "C" and game[1] == "Z":
        score += 6
        score_part_two += 7

print(score)
print(score_part_two)
