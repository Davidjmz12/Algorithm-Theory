##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 3-1-24                                                                                               #
# Subject: Algoritmia Básica                                                                                 #
# Description: contains the definition and implementation of the GenericTree class, used to save the         #
# arborescent structure obtained when applying Huffman's compression and decompression algorithm to a file   #                         
##############################################################################################################
class GenericTree:
    """
    
    Generic Tree is a class defining a generic binary tree.
    It includes methods to handle Huffman's encoding algorithm.
    
    """   
    
    def __init__(self,root,left_child,right_child):
        self.left = left_child
        self.right = right_child
        self.root = root
        
    def __str__(self):
        return self._pretty_print(self.root, 0)

    def _pretty_print(self, node, depth):
        result = "  " * depth + str(node) + "\n"

        if self.left is not None:
            result += "  " * depth + "└──l " + self.left._pretty_print(self.left.root, depth + 1)
        if self.right is not None:
            result += "  " * depth + "└──r " + self.right._pretty_print(self.right.root, depth + 1)

        return result

    def __lt__(self,other):
        return True
    def __le__(self,other):
        return True
    def __eq__(self,other):
        return True
    def __ge__(self,other):
        return True
    def __gt__(self,other):
        return True
    
    def isLeaf(self):
        """
        Pre:    True
        Post:   returns true if and only leaf self is a leaf, i.e, it has no left nor right child
        

        Time Complexity: O(1)
        
        """  
        return self.left is None and self.right is None
    
    def treeToHash(self):
        """
        Pre:    True
        Post:   returns the binary string representation of a tree
        
        
        Time Complexity: O(m) with m the number of nodes
        
        """
        return self._treeToHash("")
     
    def _treeToHash(self,code):
        """
        Pre:   code is a string containing the partial representation of a tree
        Post:   returns the binary string representation of a tree
        
        
        Time Complexity:   O(m) with m the number of nodes
        
        """  

        if self.isLeaf():
            return {self.root:code}
        else:    
            rightSide = dict() if self.right is None else  self.right._treeToHash(code+"1")
            leftSide = dict() if self.left is None else self.left._treeToHash(code+"0")
            
            leftSide.update(rightSide)
            
            return leftSide
       
    def decodeString(self,line):
        """
        Pre:    line is a binary string (one consisting of only 1's and 0's)
        Post:   returns the character codified by the binary string line
        
        
        Time Complexity: O(n) with n the length of line
        
        """  
        
        auxStr = ""
        auxTree = self
        
        for bit in line:
            if auxTree.isLeaf():
                auxStr += auxTree.root
                auxTree = self
            if bit == "0" and auxTree.left is not None:
                auxTree = auxTree.left
            elif bit == "1" and auxTree.right is not None:
                auxTree = auxTree.right
            else:
                raise Exception("Unsupported string")  
              
        if auxTree.isLeaf():     
            auxStr += auxTree.root 
        else:
            raise Exception("Unsupported string")    
           
        return auxStr