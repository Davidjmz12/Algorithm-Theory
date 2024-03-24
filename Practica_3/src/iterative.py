from variables import Variables
from shapely.geometry import Polygon, Point


class Cell:
    def __init__(self, polygon=Point((0, 0))):
        self.polygon = polygon

    @property
    def area(self):
        return self.polygon.area

    def intersects_with_pol(self, pol: Polygon):
        return pol.intersection(self.polygon).area != 0

    def max(self, cell1, cell2):
        return max([self, cell1, cell2], key=lambda x: x.area)

    def add(self, polygon):
        return Cell(self.polygon.union(polygon))


def print_matrix(matrix):
    aux = ""
    for i in matrix:
        for j in i:
            aux += str(j.area) + " "
        aux += "\n"
    print(aux)


def iterative(variable: Variables):
    mat = populate_matrix(variable)
    return (0,0,0) if variable.n==0 else (mat[int(variable.n)][int(variable.page.area)].area,0,0)


def populate_matrix(variable: Variables):
    y_dim = int(variable.page.area)
    x_dim = int(variable.n)

    iterative_matrix = [[Cell()] * y_dim]

    variable.sort_articles()

    for i in range(1, x_dim + 1):
        aux_v = [Cell()]
        a_i = int(variable.list_art[i-1].area)
        pol_i = variable.list_art[i-1].polygon

        for a in range(1, y_dim + 1):
            if a_i > a:
                aux_v += [iterative_matrix[i - 1][a]]
            else:
                if iterative_matrix[i - 1][a - a_i].intersects_with_pol(pol_i):
                    aux_v += [iterative_matrix[i - 1][a - a_i].max(Cell(pol_i), aux_v[-1])]
                else:
                    aux_v += [iterative_matrix[i - 1][a - a_i].add(pol_i)]

        iterative_matrix.append(aux_v)

    return iterative_matrix
