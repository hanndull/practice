# A robot can move only right and down in an n x n matrix. 
# It has to get to the bottom right corner of the matrix from the top left 
# corner. Write an algorithm to find the maximum number of paths it can take.

#[[0, 0, 0],
# [0, 0, 0],
# [0, 0, 0]]

# n = 3, 6 ways to go (?)
# n = 2, 2 ways to go 

# (x^2) - x ??

# smallest sequence used will always either be R + R, D + D, R + D, or D + R

# list[index][index + 1] = move right 
# list[index + 1][index] = move down

# Need to:
    # decide how to choose next path
    # track the sequences we've been through
    # know when to stop

def create_matrix(n):
    '''Creates and returns a grid of n by n size'''

    matrix = []
    to_add = []
    
    for x in range(n):
        to_add.append(0)
    
    for x in range(n):
        matrix.append(to_add.copy())
    
    return matrix

def print_matrix(matrix):
    
    for row in matrix:
        print(row)
    print()

def traverse_one_path(n):

    matrix = create_matrix(n)
    max_index = n
    r_index = 0
    d_index = 0

    while r_index < max_index and d_index < max_index:
        matrix[d_index][r_index] = 1 #shows current step
        print_matrix(matrix)
        matrix[d_index][r_index] = 2 #marks current step as having been visited
        
        if abs(r_index - d_index) == 1:
            r_index +=1 #move to next step
        else:
            d_index +=1 


def count_paths(n):
    pass



