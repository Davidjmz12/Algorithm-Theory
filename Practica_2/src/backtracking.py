from solution import Solution
from variables import Variables

def backtracking(variable: Variables, avoid_cote=False):
    
    global bestSolution
    global cases
    
    cases = 0
    bestSolution = Solution()
    initial_sol = Solution()

    backtracking_r(variable, initial_sol, avoid_cote,variable.area_page())
    
    return bestSolution.totalArea, cases

def backtracking_r(variables: Variables, thisSol: Solution, avoid_cote: bool, cote):
    
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
                    backtracking_r(variables, newSol, avoid_cote,next_cote)
                