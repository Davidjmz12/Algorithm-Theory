##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date:                                                                                                      #
# Subject: Algoritmia básica                                                                                 #
# Description:                                                                                               #
##############################################################################################################
from solution import Solution
from variables import Variables

from pulp import LpProblem, LpMaximize, LpBinary, LpVariable, lpSum, lpDot


def create_intersection_matrix(variable: Variables):
    fun = lambda i,j:0 if i==j else 0 if not variable.intersects_articles(i,j) else 1
    return [ [fun(i,j) for j in range(i, variable.n)] for i in range(variable.n)]

def linearP(variable: Variables):
    """
    
    """
    
    c_ij = create_intersection_matrix(variable)

    model = LpProblem(name="small-problem",sense=LpMaximize)
    
    n = variable.n
    
    y_i = [LpVariable(name=f"y_{i}",cat=LpBinary) for i in range(n)]
    y_ij = [[LpVariable(name=f"aux_{i}{j}",cat=LpBinary) for j in range(i,n)] for i in range(n)]
    a_i = [art.area for art in variable.list_art]
    
    objective_fun = lpSum(lpDot(a_i,y_i))
    model.setObjective(objective_fun)
    
    constraints_non_intersection = (lpSum(lpDot(y_ij,c_ij)) == 0,"no_intersection")
    model +=  constraints_non_intersection
    
    for i in range(n):
        for j in range(n-i):
            model += (y_ij[i][j] <= y_i[i],f"prod1_{i}{j}")
            model += (y_ij[i][j] <= y_i[j],f"prod2_{i}{j}")
            model += (y_ij[i][j] >= y_i[j] + y_i[i] - 1,f"prod3_{i}{j}")

    model.solve()
    
    print(model)
   
   
    return 1,2
