calories = [0]
index = 0

with open('puzzle1', 'r') as file:
    for line in file:
        if line == "\n":
            calories.append(0)
            index += 1
        else:
            calories[index] += int(line.strip())

calories = sorted(calories)

print(sum(calories[-3:]))
