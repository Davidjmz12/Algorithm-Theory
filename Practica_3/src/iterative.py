from src.variables import Variables
from shapely.geometry import Polygon, Point


class Cell:
    def __init__(self, polygon=Point((0, 0))):
        self.polygon = polygon

    @property
    def area(self):
        return self.polygon.area

    def intersects_with_pol(self, pol: Polygon):
        return pol.intersection(self.polygon).area == 0

    def max(self, polygon):
        return self if self.area > polygon.area else Cell(polygon)

    def add(self, polygon):
        return Cell(self.polygon.union(polygon))


def iterative(variable: Variables):
    mat = populate_matrix(variable)
    return mat[int(variable.n)-1][int(variable.page.area)].area


def populate_matrix(variable: Variables):
    y_dim = int(variable.page.area)
    x_dim = int(variable.n)

    iterative_matrix = [[Cell()] * y_dim]

    variable.sort_articles()

    for i in range(0, x_dim):
        aux_v = [Cell()]
        for a in range(1, y_dim + 1):

            if variable.list_art[i].area() > a:
                aux_v += [iterative_matrix[i - 1][a]]
            else:
                a_i = int(variable.list_art[i].area())
                pol_i = variable.list_art[i].polygon
                if iterative_matrix[i - 1][a - a_i].intersects_with_pol(pol_i):
                    aux_v += [iterative_matrix[i - 1][a - a_i].max(pol_i)]
                else:
                    aux_v += [iterative_matrix[i - 1][a - a_i].add(pol_i)]

        iterative_matrix.append(aux_v)

    return iterative_matrix
