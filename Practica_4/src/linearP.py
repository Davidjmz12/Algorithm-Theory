##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date:                                                                                                      #
# Subject: Algoritmia básica                                                                                 #
# Description:                                                                                               #
##############################################################################################################
from solution import Solution
from variables import Variables
import os
import sys

from pulp import LpProblem, LpMaximize, LpBinary, LpVariable, lpSum, lpDot, PULP_CBC_CMD


def create_intersection_matrix(variable: Variables):
    fun = lambda i,j:0 if i==j else 0 if not variable.intersects_articles(i,j) else 1
    return [ [fun(i,j) for j in range(i, variable.n)] for i in range(variable.n)]

def linearP(variable: Variables):
    """
    
    """
    
    
    

    model = LpProblem(name="small-problem",sense=LpMaximize)
    
    n = variable.n
    a_i = [art.area for art in variable.list_art]
    c_ij = create_intersection_matrix(variable)
    
    y_i = [LpVariable(name=f"y_{i}",cat=LpBinary) for i in range(n)]
    y_ij = [[LpVariable(name=f"aux_{i}_{j}",cat=LpBinary) for j in range(i,n)] for i in range(n)]
    
    
    objective_fun = lpSum(lpDot(a_i,y_i))
    model.setObjective(objective_fun)
    
    constraints_non_intersection = (lpSum(lpDot(y_ij,c_ij)) == 0,"no_intersection")
    model +=  constraints_non_intersection
    
    for i in range(n):
        for j in range(i,n):
            model += (y_ij[i][j-i] <= y_i[i],f"prod1_{i}_{j}") # i=0 j=1
            model += (y_ij[i][j-i] <= y_i[j],f"prod2_{i}_{j}")
            model += (y_ij[i][j-i] >= y_i[j] + y_i[i] - 1,f"prod3_{i}_{j}")

    model.solve(PULP_CBC_CMD(msg=0))
    
    index_y = [i for i in range(len(model.variables())) if model.variables()[i].name[0] == "y"]

    var_y = [model.variables()[i] for i in index_y]
    var_y.sort(key=lambda x:x.name)
    
    index_sol = [i for i in range(len(var_y)) if var_y[i].varValue == 1]

    
    return variable.area_articles(index_sol),0
