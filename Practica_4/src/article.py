##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 02-5-24                                                                                              #
# Subject: Algoritmia básica                                                                                 #
# Description: contains the definition and implementation of a class used to represent a paper's page as     #
# well as the articles that must be placed on it                                                             #
##############################################################################################################

from shapely.geometry import Polygon
from functools import cache
class Article: 
    """
    This class defines the attributes and methods of an article object representation
    
    """
    
    def __init__(self, coordinate, height, width):
        """
        Each Article consists of an origin, coordinates, a height and a width 

        """
        self.origin = coordinate
        self.height = height    
        self.width = width

    def __str__(self) -> str:
        return f"Origin:{self.origin}, Length:{self.height}, Width:{self.width}"
    
    @property  
    def polygon(self):
        """
        Pre: True
        Post: Returns a polygonal representation of self

        """
        supRight = (self.origin[0] + self.width, self.origin[1])
        botRight = (self.origin[0] + self.width, self.origin[1] + self.height)
        botLeft = (self.origin[0], self.origin[1] + self.height)
        return Polygon((self.origin, supRight, botRight, botLeft,self.origin))

    @property 
    def area(self):
        """
        Pre: True
        Post: Returns the area of self as a polygon

        """
        return self.polygon.area
    
    @cache
    def intersects(self, other_art):
        return self.polygon.intersection(other_art.polygon).area != 0
    
    def to_svg(self, color, opacity):
        """
        Pre: Color contains the hexadecimal representation of a color
        Post: Returns an svg path for a visual representation of self, with the given
        color and opacity

        """
        return self.polygon.svg(fill_color=color,opacity=opacity)

    def to_file(self) -> str:
        return (f" {self.width} {self.height} {self.origin[0]} {self.origin[1]}\n")