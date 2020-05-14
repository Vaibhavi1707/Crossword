
Black, White = '#', '_'
TO_NUMBER = Black + White + White

def add_sentinels(grid) :
    size = len(grid[0])
    sentinel_grid = [Black + row + Black for row in grid]
    sentinel_grid.append((size+2) * Black)
    sentinel_grid.insert(0, (size + 2) * BLACK)
    return sentinel_grid

def clue_positions(grid):
    def isClue(row, col):
        return grid[col - 1 : col + 2] == TO_NUMBER or grid[row - 1][col] + grid[row][col] + grid[row + 1][col] == TO_NUMBER
    
    cluePositions = []
    for row in range(len(grid)):
        for col in range(len(row)):
            if isClue(row, col) :
                cluePositions.append(row, col)
    return cluePositions


def grid_generator(locations):
    grid = [['_' for i in range(15)] for j in range(15)]
    
    for i, j in locations:
        grid[i][j] = '#'
    
    return clue_positions(grid)

print(grid_generator(input()))