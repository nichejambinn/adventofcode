score = 0

# where first key is opponent's move and second is your move (rock, paper, scissors)
points_move = {
    ('A','X'): 1 + 3,
    ('A','Y'): 2 + 6,
    ('A','Z'): 3 + 0,
    ('B','X'): 1 + 0,
    ('B','Y'): 2 + 3,
    ('B','Z'): 3 + 6,
    ('C','X'): 1 + 6,
    ('C','Y'): 2 + 0,
    ('C','Z'): 3 + 3,
}

# where first key is opponent's move and second is the outcome (lose, draw, win)
points_outcome = {
    ('A','X'): 3 + 0,
    ('A','Y'): 1 + 3,
    ('A','Z'): 2 + 6,
    ('B','X'): 1 + 0,
    ('B','Y'): 2 + 3,
    ('B','Z'): 3 + 6,
    ('C','X'): 2 + 0,
    ('C','Y'): 3 + 3,
    ('C','Z'): 1 + 6,
}

with open('puzzle2', 'r') as file:
    for line in file:
        move, response = line.split()
        score += points_outcome[(move, response)]

print(score)