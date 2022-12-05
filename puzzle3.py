from functools import reduce

total = 0

# map items to their priority
lower_priority = { chr(96 + i): i for i in range(1,27)}
upper_priority = { chr(64 + i): i+26 for i in range(1,27)}

priority = lower_priority.copy()
priority.update(upper_priority)

# parse input
with open('puzzle3', 'r') as file:
    # part 1
    # for line in file:
    #     # convert the two halves of each line into a set of the unique elements
    #     c1 = set(line[:len(line)//2])
    #     c2 = set(line[len(line)//2:])

    #     # find the intersection
    #     shared = c1 & c2
        
    #     # total the priority of the shared items
    #     total += priority[shared.pop()]

    # part 2
    input = file.readlines()
    # get each triplet of lines as sets and take the priority of their intersection
    for i in range(0, len(input), 3):
        badge = reduce(set.intersection, map(set, input[i:i+3]))
        badge.remove('\n')
        total += priority[badge.pop()]
        
print(total)