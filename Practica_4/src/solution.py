##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 24-03-24                                                                                             #
# Subject: Algoritmia básica                                                                                 #
# Description: contains the definition and implementation of a class used to represent the solutions of our  #
# backtracking problem                                                                                       #
##############################################################################################################

class Solution:
    """
    Definition and implementation of a class used to represent 
    the solution of our backtracking problem

    """

    def __init__(self, indexes=[], totalArea=0):
        self.indexes = indexes
        self.totalArea = totalArea

    def __eq__(self, other) -> bool:
        """
        Pre: self and other are instances of the Solution class
        Post: Returns True if and only if both solutions have the same total area

        """
        return self.totalArea == other.totalArea and self.indexes != other.indexes

    def __gt__(self, other) -> bool:
        """
        Pre: self and other are instances of the Solution class
        Post: Returns true if and only if self's total area is greater than other's

        """
        return self.totalArea > other.totalArea

    def __lt__(self, other) -> bool:
        """
        Pre: self and other are instances of the Solution class
        Post: Returns true if and only if self's total area is lesser than other's

        """
        return self.totalArea < other.totalArea

    def last(self):
        return self.indexes[-1]
    
    def __str__(self):
        return f"Indexes: {self.indexes}, Area: {self.totalArea}"
