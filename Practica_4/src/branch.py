##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date:                                                                                                      #
# Subject: Algoritmia básica                                                                                 #
# Description:                                                                                               #
##############################################################################################################
from solution import Solution
from variables import Variables
import heapq as hq


def cost_function(sol:Solution, variable:Variables):
    """
    
    """
    return variable.area_page()-variable.bound(sol)

def estimation_function(sol:Solution, variable:Variables):
    """
    
    """
    return variable.area_page()-variable.bound_2(sol)

def branch(variable: Variables):
    """
    
    """
    cote = float('inf')
    branches=0
    solution = Solution()
    queue = []
    
    # We add the first variables
    for i in range(variable.n):
        node = Solution([i],variable.area_article(i))
        hq.heappush(queue, (estimation_function(node,variable),node))
    
    
    while queue:
        node_id = hq.heappop(queue)[1]
        branches += 1
        for i in range(node_id.next,variable.n):
            #If it is a feasible solution
            if variable.article_fits(i,node_id):
                child = Solution(node_id.indexes + [i],node_id.totalArea + variable.area_article(i))
                # If it is not pruned
                if estimation_function(child,variable) <= cote:
                    hq.heappush(queue, (estimation_function(child, variable),child))
                    
                    cost_child = cost_function(child,variable)
                    if cost_child<cote:
                        cote = cost_child
                        solution=child
        
        if not queue or estimation_function(hq.nsmallest(1,queue)[0][1], variable) >= cote:
            return solution.totalArea,branches
    
    print("Solution not found!!")
    exit(-1)

    