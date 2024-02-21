from solution import Solution
from variables import Variables

def backtracking(variable: Variables, avoid_cote=False):
    
    global bestSolution
    global cases
    
    cases = 0
    bestSolution = Solution()
    initial_sol = Solution()

    backtracking_r(variable, initial_sol, avoid_cote)
    
    return bestSolution.totalArea, cases

def backtracking_r(variables: Variables, thisSol: Solution, avoid_cote: bool):
    
    global bestSolution
    global cases
    cases += 1
    
    for i in range(thisSol.next, variables.n):
        
        if variables.article_fits(i,thisSol):
            
            newSol = Solution(thisSol.indexes+[i], thisSol.totalArea + variables.area_article(i))
            if newSol > bestSolution:
                bestSolution = newSol
            
            if i < variables.n-1:
                if avoid_cote or variables.cote(newSol) > bestSolution.totalArea:
                    backtracking_r(variables, newSol, avoid_cote)
                