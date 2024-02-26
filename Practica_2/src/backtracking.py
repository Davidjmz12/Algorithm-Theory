##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 24-2-24                                                                                              #
# Subject: Algoritmia básica                                                                                 #
# Description: contains the implementation of a backtracking algorithm that computes the articles that must  #
# be placed on a paper's page to use the maximum area possible                                               #
##############################################################################################################
from solution import Solution
from variables import Variables

def backtracking(variable: Variables, avoid_cote=False):

    """
    Pre: variable contains all the necessary information to compute which articles must be placed 
    in a paper page to use the maximum space possible.
    Post: Returns the total area occupied by the chosen articles and the number of tree nodes, considering the
    arborescent representation of a backtrackig algorithm, visited during its computation

    """
    
    global bestSolution
    global cases
    
    cases = 0
    bestSolution = Solution()
    initial_sol = Solution()

    backtracking_r(variable, initial_sol, avoid_cote, variable.area_page())
    
    return bestSolution.totalArea, cases

def backtracking_r(variables: Variables, thisSol: Solution, avoid_cote: bool, cote):

    """
    Recursive backtracking algorithm that, given an instance of the class Variables which contains all the necessary
    information to compute which articles must be placed in a paper page to use the maximum space possible, 
    returns the total area occupied by the chosen articles and the number of tree nodes, considering the
    arborescent representation of a backtrackig algorithm, visited during its computation
    
    """
    
    global bestSolution
    global cases
    
    for i in range(thisSol.next, variables.n):
        cases += 1
        
        if cote <= bestSolution.totalArea:
            return
        
        if variables.article_fits(i,thisSol):
            
            newSol = Solution(thisSol.indexes+[i], thisSol.totalArea + variables.area_article(i))
            if newSol > bestSolution:
                bestSolution = newSol
            
            if i < variables.n-1:
                next_cote = variables.cote(newSol)
                if avoid_cote or cote > bestSolution.totalArea:
                    backtracking_r(variables, newSol, avoid_cote, next_cote)
                