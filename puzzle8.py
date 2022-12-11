from functools import reduce

def find_num_visible_trees(forest):
    visible_trees = [ [0 for _ in forest[0]] for _ in forest]
    
    # a tree is visible if it is visible for the left, right, top or bottom
    # a tree is visible from a given direction if it is taller than the tallest tree before it
    for j in range(len(forest)):
        tallest_tree = -1
        for i in range(len(forest[0])):
            if forest[j][i] > tallest_tree:
                visible_trees[j][i] = 1
                tallest_tree = forest[j][i]

    for j in range(len(forest)):
        tallest_tree = -1
        for i in range(len(forest[0])-1, 0, -1):
            if forest[j][i] > tallest_tree:
                visible_trees[j][i] = 1
                tallest_tree = forest[j][i]

    for i in range(len(forest[0])):
        tallest_tree = -1
        for j in range(len(forest)):
            if forest[j][i] > tallest_tree:
                visible_trees[j][i] = 1
                tallest_tree = forest[j][i]

    for i in range(len(forest[0])):
        tallest_tree = -1
        for j in range(len(forest)-1, 0, -1):
            if forest[j][i] > tallest_tree:
                visible_trees[j][i] = 1
                tallest_tree = forest[j][i]

    num_visible_trees = sum([sum(row) for row in visible_trees])
    return num_visible_trees


def calculate_scenic_score(forest, row, col):
    score = [0,0,0,0]
    orig_col = col
    orig_row = row

    tree_height = forest[row][col]

    # check left
    while col > 0:
        if forest[row][col-1] >= tree_height:
            score[0] += 1
            break
        score[0] += 1
        col -= 1
    col = orig_col

    # check right
    while col < len(forest[0])-1:
        if forest[row][col+1] >= tree_height:
            score[1] += 1
            break
        score[1] += 1
        col += 1
    col = orig_col

    # check up
    while row > 0:
        if forest[row-1][col] >= tree_height:
            score[2] += 1
            break
        score[2] += 1
        row -= 1
    row = orig_row

    # check down
    while row < len(forest)-1:
        if forest[row+1][col] >= tree_height:
            score[3] += 1
            break
        score[3] += 1
        row += 1

    return reduce(lambda x,y: x*y, score)


def max_scenic_score(forest):
    max_score = 0
    for row in range(len(forest)):
        for col in range(len(forest[0])):
            scenic_score = calculate_scenic_score(forest, row, col)
            max_score = max(max_score, scenic_score)

    return max_score


if __name__=='__main__':
    with open('puzzle8', 'r') as file:
        forest = []
        for line in file:
            forest.append([int(n) for n in line.strip()])

        print(find_num_visible_trees(forest)) # part 1
        print(max_scenic_score(forest)) # part 2
