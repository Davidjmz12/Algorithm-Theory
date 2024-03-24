##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 24-2-24                                                                                              #
# Subject: Algoritmia básica                                                                                 #
# Description: contains the implementation of a backtracking algorithm that computes the articles that must  #
# be placed on a paper's page to use the maximum area possible                                               #
##############################################################################################################
from solution import Solution
from variables import Variables


def recursive(variable: Variables):
    """

    """
    global cases
    cases = 0

    initial_sol = Solution()
    sol = recursive_r(variable, 0, initial_sol)
    return sol.totalArea, len(sol.indexes), cases


def recursive_r(variables: Variables, i: int, thisSol: Solution):
    """
    """
    global cases
    cases += 1

    if i == variables.n:
        return thisSol

    if variables.article_fits(i, thisSol):
        newSol = Solution(thisSol.indexes + [i], thisSol.totalArea + variables.area_article(i))
        return max(recursive_r(variables, i + 1, newSol), recursive_r(variables, i + 1, thisSol),
                   key=lambda x:x.totalArea)
    else:
        return recursive_r(variables, i + 1, thisSol)
