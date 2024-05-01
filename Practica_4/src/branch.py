##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date:                                                                                                      #
# Subject: Algoritmia básica                                                                                 #
# Description:                                                                                               #
##############################################################################################################
from solution import Solution
from variables import Variables
import heapq as hq


def cost_function(indexes, variable:Variables):
    """
    
    """
    
    return 1

def estimation_function():
    """
    
    """
    
    return 1

def branch(variable: Variables):
    """
    
    """

    cote = float('inf')
    branches=0
    solution = Solution()
    queue = []
    
    # We add the first variables
    for i in range(1,variable.n):
        node = Solution([i],variable.area_article(i))
        hq.heappush(queue, (estimation_function(node,variable),[i]))
    
    
    while queue:
        node_id = hq.heappop(queue)
        branches += 1
        for i in range(node_id.last()+1,variable.n):
            #If it is a feasible solution
            if variable.article_fits(i,node_id):
                child = Solution(node_id + [i],node_id.totalArea + variable.area_article(i))
                # If it is not pruned
                if estimation_function(child) <= cote:
                    hq.heappush(queue, (estimation_function(child)),child)
                    
                    cost_child = cost_function(child)
                    if cost_child<cote:
                        cote = cost_child
                        solution=child
        
        if not queue or estimation_function(hq.nsmallest(1,queue)[0][1]) >= cote:
            return solution.totalArea,branches
    


    