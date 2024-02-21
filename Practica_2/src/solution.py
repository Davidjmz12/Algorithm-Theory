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