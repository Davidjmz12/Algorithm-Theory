##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 7-4-24                                                                                              #
# Subject: Algoritmia básica                                                                                 #
# Description: contains the definition and implementation of the iterative algorithm for the article problem #
##############################################################################################################



from variables import Variables
from shapely.geometry import Polygon, Point


class Cell:
    """
    Class that contains a polygon representing the solution.
    With this class the matrix of the dynamic problem will be made.
    
    """
    def __init__(self, _polygon=Point((0, 0)),_indexes=[]):
        self.polygon = _polygon
        self.indexes = _indexes

    @property
    def area(self):
        return self.polygon.area

    def intersects_with_pol(self, pol: Polygon):
        return pol.intersection(self.polygon).area != 0

    def max(self, cell1, cell2):
        return max([self, cell1, cell2], key=lambda x: x.area)

    def add(self, polygon,ind):
        return Cell(self.polygon.union(polygon),self.indexes+[ind])

# ---------------------------------------------------------------------------------------------
# Auxiliary Functions
# ---------------------------------------------------------------------------------------------

def print_matrix(matrix):
    
    """
    Function that prints matrix, a 2-D array of the class Cell
    """
    aux = ""
    for i in matrix:
        for j in i:
            aux += str(j.area) + " "
        aux += "\n"
    print(aux)

def plot_matrix(matrix):
    """
    Function that plots matrix, a 2-D array of the class Cell
    """
    import numpy as np
    import matplotlib.pyplot as  plt
    
    np_array = np.array([[obj.area for obj in row] for row in matrix])
    plt.pcolormesh(np_array, cmap='viridis')
    plt.colorbar()
    plt.show()

def populate_matrix(variable: Variables):
    
    """
    Function that populates the matrix that will be used to solve the problem.
    
    """
    y_dim = int(variable.page.area)
    x_dim = int(variable.n)

    iterative_matrix = [[Cell()] * (y_dim+1)]

    variable.sort_articles()

    # For each row
    for i in range(0, x_dim):
        aux_v = [Cell()]
        a_i = int(variable.list_art[i].area)
        pol_i = variable.list_art[i].polygon
        
        # For each column
        for a in range(1, y_dim + 1):
            if a_i > a:
                aux_v += [iterative_matrix[i][a]]
            else:
                if iterative_matrix[i][a - a_i].intersects_with_pol(pol_i):
                    aux_v += [iterative_matrix[i][a - a_i].max(Cell(pol_i), aux_v[-1])]
                else:
                    aux_v += [iterative_matrix[i][a - a_i].add(pol_i,i)]

        iterative_matrix.append(aux_v)

    return iterative_matrix

# ---------------------------------------------------------------------------------------------

def iterative(variable: Variables):
    """
    Dynamic callable function
    
    Pre: variable contains the variables of the problem
    Post: Returns the result of the Dynamic problem.
    
    Time complexity: O(n*N) where N is the total area of the article and
                     n is the number of articles.
    """
    
    if variable.n==0:
        return (0,"")
    
    mat = populate_matrix(variable)
    sol_cell = mat[int(variable.n)][int(variable.page.area)]
    
    return sol_cell.area, variable.to_file(sol_cell)