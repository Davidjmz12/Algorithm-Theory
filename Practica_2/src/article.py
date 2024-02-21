from shapely.geometry import Polygon
              
class Article: 
    """
    This class defines the attributes and methods of an article object representation
    
    """
    
    def __init__(self, coordinate, height, width):
        self.origin = coordinate
        self.length = height    
        self.width = width

    def __str__(self) -> str:
        return f"Origin:{self.origin}, Length:{self.length}, Width:{self.width}"
    
    @property  
    def polygon(self):
        supRight = (self.origin[0] + self.width, self.origin[1])
        botRight = (self.origin[0] + self.width, self.origin[1] + self.length)
        botLeft = (self.origin[0], self.origin[1] + self.length)
        return Polygon((self.origin, supRight, botRight, botLeft,self.origin))

    def area(self):
        return self.polygon.area
    
    def to_svg(self, color,opacity):
        return self.polygon.svg(fill_color=color,opacity=opacity)
