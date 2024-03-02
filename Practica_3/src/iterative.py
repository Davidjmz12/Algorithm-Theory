from variables import Variables
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


def populate_matrix(variables: Variables):
    y_dim = variables.page.area
    x_dim = variables.n

    iterative_matrix = [[Cell()] * y_dim]

    variables.sort_articles()

    for i in range(0, x_dim + 1):
        aux_v = [Cell(0)]
        for a in range(0, y_dim + 1):

            if variables.list_art[i].area > a:
                aux_v += iterative_matrix[i - 1][a]
            else:
                a_i = int(variables.list_art[i].area)
                pol_i = variables.list_art[i].polygon
                if iterative_matrix[i - 1][a - a_i].intersects_with_pol(pol_i):
                    aux_v += iterative_matrix[i - 1][a - a_i].max(pol_i)
                else:
                    aux_v += iterative_matrix[i - 1][a - a_i].add(pol_i)

        iterative_matrix.append(aux_v)

    return iterative_matrix
