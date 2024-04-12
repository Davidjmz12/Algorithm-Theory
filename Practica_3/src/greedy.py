##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 24-3-24                                                                                              #
# Subject: Algoritmia básica                                                                                 #
# Description: contains the implementation of a greedy heuristic algorithm that computes the articles that   #
# must be placed on a paper's page to use the maximum area possible                                          #
##############################################################################################################

from solution import Solution
from variables import Variables


def greedy(variable: Variables):
    """
    Greedy callable function.
    Pre: variable contains the variables of the article-problem
    Post: Return 3 values: the total area, the number of articles of the solution and the number of iterations
          made in the algorithm.
          
    Time Complexity: O(n) where n is the number of articles.
    """

    initial_sol = Solution()
    variable.sort_articles(_reverse=True)
    
    sol = greedy_r(variable,[], initial_sol)
    return sol.totalArea, variable.to_file(sol)


def greedy_r(variable: Variables, articles_not_ind, thisSol: Solution):
    """
    Greedy auxiliary function
    Pre: variable contains the variables of the problem
         articles_not_ind is a list of the index of the articles that do not fit in the solution
         thisSol contains a solution already made.
    Post: return the best solution out of all the possibles ones in variables.
    """


    # If non article is possible
    if variable.n == len(articles_not_ind):
        return thisSol

    
    possible_articles = [i for i in range(variable.n) if i not in articles_not_ind]
    
    candidate_index = possible_articles[0]
    candidate_area = variable.area_article(candidate_index)
    
    intersection_with_candidate_index = [i for i in possible_articles if variable.intersects_articles(i,candidate_index) and i != candidate_index]
    
    sum_areas_intersection = sum([variable.area_article(i) for i in intersection_with_candidate_index])
    
    if candidate_area>sum_areas_intersection:
        new_sol = Solution(thisSol.indexes+[candidate_index],thisSol.totalArea+candidate_area)
        return greedy_r(variable,articles_not_ind+intersection_with_candidate_index+[candidate_index],new_sol)
    else:
        return greedy_r(variable,articles_not_ind+[candidate_index],thisSol)
