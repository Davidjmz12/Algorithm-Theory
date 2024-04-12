##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 24-3-24                                                                                              #
# Subject: Algoritmia básica                                                                                 #
# Description: contains the implementation of a backtracking algorithm that computes the articles that must  #
# be placed on a paper's page to use the maximum area possible                                               #
##############################################################################################################
from solution import Solution
from variables import Variables


def recursive(variable: Variables):
    """
    Recursive callable function.
    Pre: variable contains the variables of the article-problem
    Post: Return 2 values: the total area and a string with the articles in the solution. 
          
    Time Complexity: O(2^n) where n is the number of articles.
    
    """
    global cases
    cases = 0

    initial_sol = Solution()
    sol = recursive_r(variable, 0, initial_sol)
    return sol.totalArea, variable.to_file(sol)


def recursive_r(variable: Variables, i: int, thisSol: Solution):
    """
    Recursive auxiliary function
    Pre: variable contains the variables of the problem
         i is an index of the article to select
         thisSol contains a solution already made.
    Post: return the best solution out of all the possibles ones in variables.
    """
    
    global cases
    cases += 1

    if i == variable.n:
        return thisSol

    if variable.article_fits(i, thisSol):
        newSol = Solution(thisSol.indexes + [i], thisSol.totalArea + variable.area_article(i))
        return max(recursive_r(variable, i + 1, newSol), recursive_r(variable, i + 1, thisSol),
                   key=lambda x:x.totalArea)
    else:
        return recursive_r(variable, i + 1, thisSol)
