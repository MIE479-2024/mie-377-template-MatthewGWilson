import cvxpy as cp
import numpy as np

def MVO(mu, Q, short):
    # find the total number of assets
    n = len(mu)

    # set the target as the average expected return of all assets
    targetRet = np.mean(mu)

    # add the expected return constraint
    A = -1 * mu.T
    b = -1 * targetRet

    # constrain weights to sum to 1
    Aeq = np.ones([1, n])
    beq = 1

    # define the variable for asset weights
    x = cp.Variable(n)

    # set up the constraints list
    constraints = [
        A @ x <= b,
        Aeq @ x == beq
    ]

    # apply long/short constraints based on the `short` list
    for i in range(n):
        if short[i] == 0:
            # Long position constraint (non-negative weight)
            constraints.append(x[i] >= 0)
        else:
            # Short position constraint (non-positive weight)
            constraints.append(x[i] <= 0)

    # define and solve the optimization problem
    prob = cp.Problem(cp.Minimize((1 / 2) * cp.quad_form(x, Q)), constraints)
    
    prob.solve(verbose=False)
    return x.value