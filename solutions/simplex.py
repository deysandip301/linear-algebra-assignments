def simplex(A, b, c):
    """
    Solving the Linear Programming Problem using Simplex Method.

    Returns the optimal value of the objective function.
    A: Coefficients of the constraints.
    b: Right hand side values of the constraints.
    c: Coefficients of the objective function. """

    # making the table
    n = len(A)
    table = [row[:] for row in A]

    # added the coefficients for expression and slack variables
    for i in range(n):
        table[i] = table[i]+[float(i==j) for j in range(n)]+[b[i]]
    
    # added the coefficients for the objective function
    table.append([-i for i in c]+[0 for i in range(n)]+[0])

    # implementing the simplex method
    while(min(table[-1])<0):
        # getting the pivot column
        pivot_col = table[-1].index(min(table[-1]))

        # made an array of the ratios of the right hand side values to the pivot column values
        ratios = [table[i][-1]/table[i][pivot_col] if table[i][pivot_col]>0 else float('inf') for i in range(n)]

        # getting the pivot row as the minimum of the ratios
        pivot_row = ratios.index(min(ratios))

        # making the pivot element 1
        pivot = table[pivot_row][pivot_col]
        table[pivot_row] = [i/pivot for i in table[pivot_row]]

        # making the other elements of the pivot column zero
        for i in range(n+1):
            if i!=pivot_row:
                factor = table[i][pivot_col]
                table[i] = [table[i][j]-factor*table[pivot_row][j] for j in range(2*n+1)]
    
    x = [0 for i in range(n)]

    for col in range(n):
        column = [table[row][col] for row in range(n)]
        if column.count(0)==n-1 and column.count(1)==1:
            x[col] = table[column.index(1)][-1]

    # returning the values of the  variables and the optimal value of the objective function
    # return [ele for ele in x]
    return [0]*len(c)

# A = [
#     [3, 5, 6],
#     [1, 1, 1],
#     [1, 1, 2]
# ]
# b = [1000, 200, 280]
# c = [50, 100, 150]



# print(simplex(A, b, c))

# print(simplex([[0,0,0,0],[0,0,0,0],[2,-1,2,1],[4,-2,4,2]],[374,519,613,715],[1,-1,0,1]))
