# A robot can move only right and down in an n x n matrix. 
# It has to get to the bottom right corner of the matrix from the top left 
# corner. Write an algorithm to find the maximum number of paths it can take.

#[[0, 0, 0],
# [0, 0, 0],
# [0, 0, 0]]
# n = 3, 6 ways to go (?)

# smallest sequence used will always either be R + R, D + D, R + D, or D + R

# list[index][index + 1] = move right 
# list[index + 1][index] = move down

# Need to:
    # decide how to choose next path
    # track the sequences we've been through
    # know when to stop

def create_matrix(n):
    matrix = []
    to_add = []
    
    for x in range(n):
        to_add.append(0)
    
    for x in range(n):
        matrix.append(to_add)
    
    return matrix







