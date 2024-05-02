##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 02-5-24                                                                                              #
# Subject: Algoritmia básica                                                                                 #
# Description:  Implementation of the Branch and Prune algorithm                                             #
##############################################################################################################
from solution import Solution
from variables import Variables
import heapq as hq


def cost_function(sol:Solution, variable:Variables):
    """
    Function that returns the cost_function of the solution 'sol'
    
    """
    return variable.area_page()-sol.totalArea

def estimation_function(sol:Solution, variable:Variables):
    """
    Function that returns the estimation functuon of the solution 'sol'
    
    """
    return variable.area_page()-sol.totalArea-variable.bound_2(sol)

def branch(variable: Variables):
    """
    Function that returns the total area and the number of expanded branches 
    
    """
    
    cote = float('inf')
    branches=0
    solution = Solution()
    queue = []
    
    # We add the first variables
    hq.heappush(queue,(0,0,Solution()))
    
    while queue:
        node_id = hq.heappop(queue)[2]
        branches += 1
        for i in range(node_id.next,variable.n):
            #If it is a feasible solution
            if variable.article_fits(i,node_id):
                child = Solution(node_id.indexes + [i],node_id.totalArea + variable.area_article(i))
                # If it is not pruned
                if estimation_function(child,variable) <= cote:
                    hq.heappush(queue, (estimation_function(child, variable),variable.n-len(child.indexes),child))
                    
                    cost_child = cost_function(child,variable)
                    if cost_child<cote:
                        cote = cost_child
                        solution=child
        
        if not queue or estimation_function(hq.nsmallest(1,queue)[0][2], variable) >= cote:
            return solution.totalArea,branches
    
    print("Solution not found!!")
    exit(-1)

    