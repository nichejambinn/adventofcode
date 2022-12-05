count = 0

test = 0

with open('puzzle4', 'r') as file:
    for line in file:
        sections = [ tuple(map(int, pair.split('-'))) for pair in line.split(',') ]

        # part 1 - containment
        # if sections[1][1] >= sections[0][1] and sections[1][0] <= sections[0][0]:
        #     # second section contains first
        #     count += 1
        # elif sections[0][1] >= sections[1][1] and sections[0][0] <= sections[1][0]:
        #     # first section contains second
        #     count += 1

        # part 2 - overlap
        if sections[1][0] <= sections[0][1] and sections[1][1] >= sections[0][0]:
            count += 1

print(count)