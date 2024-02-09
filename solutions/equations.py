# Do NOT use any external libraries

def solve(A, b):
    """A is a m x n matrix, and b is an n x 1 vector.
    returns: x, where x is the solution to the equation Ax = b
    if no solution exists, return -1
    if infinite solutions exist, return -2"""
    if(len(A[0]) != len(b)):
        return "Invalid input"
    

    
    # coping the elements of the matrix A to augmented_matrix
    augmented_matrix = [ele for ele in A]

    # appending the elements of the matrix B to the augmented_matrix
    for i in range(len(augmented_matrix)):
        augmented_matrix[i].append(b[i])

    # initialize the solution to True and we can change it to False later
    solution = True

    
    # Applying Gauss-Jordan elimination
    for pivot in range(len(augmented_matrix)) :

        if(augmented_matrix[pivot][pivot] == 0):
            # we have to swap the rows if possible

            for row in range(pivot+1,len(augmented_matrix)):
                if(augmented_matrix[row][pivot] != 0):
                    augmented_matrix[pivot],augmented_matrix[row] = augmented_matrix[row],augmented_matrix[pivot]
                    break


        #if the pivot is still zero that is we didn't find any row to swap with
        if(augmented_matrix[pivot][pivot] == 0):
            solution = False
            continue

        # we have to make the pivot 1 by dividing the row by the pivot
        augmented_matrix[pivot] = [ele/augmented_matrix[pivot][pivot] for ele in augmented_matrix[pivot]]

        # we have to make the all the columns values zero except the pivot
        for row in range(len(augmented_matrix)):
            if(row != pivot and augmented_matrix[row][pivot] != 0):
                factor = augmented_matrix[row][pivot]
                augmented_matrix[row] = [augmented_matrix[row][col] - factor*augmented_matrix[pivot][col] for col in range(len(augmented_matrix[row]))]

        
        # now we have to check if the solution is True or False
                
    if(solution):
        return [ele[-1] for ele in augmented_matrix]
    else :
        for row in range(len(augmented_matrix)):
            if(augmented_matrix[row][row] != augmented_matrix[row][-1]):
                return -1   # no solution
            
        return -2   # infinite solutions
    x = [0] * len(A[0])
    return x


def det(A):
    """calculates the determinant of A
    if A is not a square matrix, return 0"""
    if(len(A) != len(A[0])):
        return 0
    
    n = len(A)

    # intitializing the value of determinant from 1
    det = 1

    for i in range(n):
        # taking the value of pivot element
        pivot = A[i][i]

        # if the pivot element is zero we have to swap the rows
        if(pivot == 0):
            for j in range(i+1,n):
                if(A[j][i] != 0):
                    A[i],A[j] = A[j],A[i]
                    det *= -1
                    break
        
        # if swaping is not possible then the determinant is zero
        if(A[i][i] == 0):
            return 0
        

        # muntiplying the determinant by the pivot element
        det *= A[i][i]

        # making the pivot element 1
        A[i] = [ele/A[i][i] for ele in A[i]]

        # making the all the columns values zero except the pivot
        for j in range(n):
            if(j != i and A[j][i] != 0):
                factor = A[j][i]
                A[j] = [A[j][k] - factor*A[i][k] for k in range(n)]

    return det
    return 0
