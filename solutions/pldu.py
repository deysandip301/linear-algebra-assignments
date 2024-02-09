def pldu(A):
    """
    Decomposing a matrix A into its PLUD form.
    """
    n = len(A)
    
    # initialising P as Identity matrix
    P = [[float(i==j) for j in range(n)] for i in range(n)]

    # initialising L as Identity matrix
    L = [[float(i==j) for j in range(n)] for i in range(n)]
    
    # initialising U as a copy of A matrix
    U = [row[:] for row in A]

    # making the D matrix
    D = [[0 for j in range(n)] for i in range(n)]

    # making the P, L and U matrices
    for pivot in range(n):
        
        # check if the pivot is 0
        if U[pivot][pivot]==0:
            # swap rows
            for row in range(pivot, n):
                if U[row][pivot]!=0:
                    U[pivot], U[row] = U[row], U[pivot]
                    P[pivot], P[row] = P[row], P[pivot]
                    for i in range(pivot):
                        L[pivot][i], L[row][i] = L[row][i], L[pivot][i]
                    break
            else:
                return -1
        

        factor = U[pivot][pivot]
        D[pivot][pivot] = factor

        # making the pivot 1
        U[pivot] = [(elem/U[pivot][pivot]) for elem in U[pivot]]

        # making the other elements of the pivot column zero
        for row in range(pivot, n):
            if row!=pivot and U[row][pivot]!=0:
                L[row][pivot] = U[row][pivot]/factor
                U[row] = [(U[row][i]-U[pivot][i]*U[row][pivot]) for i in range(n)]
    
    # transpose of P
    inv_P = [[P[j][i] for j in range(n)] for i in range(n)]

    return inv_P, L, D, U