from solution import Solution,Solutions
from variables import Variables

def backtracking(variable: Variables):
    
    global bestSolutions
    bestSolutions = Solutions()
    
    initial_sol = Solution()

    backtracking_r(variable, initial_sol)
    
    return bestSolutions.totalArea

def backtracking_r(variables: Variables, thisSol: Solution):
    
    global bestSolutions
    
    if variables.cote(thisSol) > bestSolutions.totalArea:   
             
        for i in range(thisSol.next, variables.n):
            
            if variables.article_fits(i,thisSol):
                
                newSol = Solution(thisSol.indexes+[i], thisSol.totalArea + variables.area_article(i))
                
                if i == variables.n-1:
                    bestSolutions.update(newSol)
                else:
                    backtracking_r(variables, newSol)
            else:
                bestSolutions.update(thisSol)
