import re

stacks = { i:[] for i in range(1,10)}

with open('puzzle5', 'r') as file:
    lines = file.readlines()

    # fill stacks
    for i in range(7,-1,-1):
        for k in range(1, len(lines[0]), 4):
            if lines[i][k] != " ":
                stacks[k//4+1].append(lines[i][k])

    # follow instructions
    for i in range(10,len(lines)):
        # get instruction values 'move x from y to z'
        ins = re.search(r'move (\d+) from (\d+) to (\d+)', lines[i])
        x,y,z = int(ins.group(1)), int(ins.group(2)), int(ins.group(3))

        # part 1 - move crates one at a time
        # while x > 0:
        #     stacks[z].append(stacks[y].pop())
        #     x -= 1

        # part 2 - move crates as a unit
        # add the unit onto the end of the target stack
        stacks[z].extend(stacks[y][x*-1:])
        # keep only the remaining bottom units from the source stack
        stacks[y] = stacks[y][:len(stacks[y])-x]

print(''.join([stacks[i].pop() for i in range(1,len(stacks)+1)]))
