class Solutions:
    
    def __init__(self):
        self.solutions = [Solution([],0)]
    
    @property
    def totalArea(self):
        return self.solutions[0].totalArea
    
    def update(self,other_sol):
        if other_sol > self.solutions[0]:
            self.solutions = [other_sol]
        elif other_sol == self.solutions[0]:
            self.solutions.append(other_sol)
            

class Solution:
    
    def __init__(self, indexes = [], totalArea = 0):
        self.indexes = indexes
        self.totalArea = totalArea
    
    def __eq__(self, other) -> bool:
        return self.totalArea == other.totalArea  and self.indexes != other.indexes

    def __gt__(self, other) -> bool:
        return self.totalArea > other.totalArea
    
    def __lt__(self, other) -> bool:
        return self.totalArea < other.totalArea

    def __str__(self):
        return f"Indexes: {self.indexes}, Area: {self.totalArea}"
    
    @property
    def next(self):
        if len(self.indexes) == 0:
            return 0
        else:
            return self.indexes[-1]+1