##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 3-1-24                                                                                               #
# Subject: Algoritmia básica                                                                                 #
# Description: contains the definition and implementation of auxiliary functions used to develop             #
# Huffman's compression and decompression algorithm                                                          #
##############################################################################################################

from bitArray import BitArray
import pickle
from generic_tree import GenericTree
import heapq

def getBinaryStringFromTree(tree: GenericTree) -> str:
    """
    Pre:    tree contains the tree obtained from applying the Huffman compression algorithm to a 
            file.
    Post:   returns the binary string (a string consisting of only 0's and 1's) representation of 
            tree
    
    
    Time Complexity: O(m) where m is the the number of tree nodes.
    
    """  
    
    binary_tree = pickle.dumps(tree)
    string_binary_tree = BitArray(bytes=binary_tree).bin
    length_tree = int(len(string_binary_tree)/8)
    tree_header = numberToMString(length_tree,4*8)
    
    return tree_header + string_binary_tree

def getEncodedString(nameInputF: str, hashMap: dict) -> str: 
    """
    Pre:    nameInputF contains the name of the file which we need to decompress and hasMap contains the binary 
            representation of each character that appeared on the original file
    Post:   returns the decompressed content of nameInputF
    
    
    Time Complexity: O(n*m) with n the length of nameInputF  and m the length of the hashMap
    
    """  

    with open(nameInputF,"r") as f_input:
        encode_output = ""
        for c in f_input.read():
            encode_output += hashMap[c]  # The average access time complexity is O(1) but in the worst case is O(m)
        return encode_output


def ParseFile(file: str) -> dict:
    """
    Pre:    file contains the name of the file to which we want to apply the Huffman compression algorithm 
    Post:   returns a hashmap that contains, for each character on the file, its frequency on the file.
    
    
    Time Complexity: O(n*m) where n is the length of the file by name "file" and m is the length of the hashmap
    
    """  

    mapFile = {}
    with open(file,"r") as f:     
        for x in f.read():
            if x in mapFile:
                mapFile[x] = mapFile[x] + 1
            else:
                mapFile[x] = 1
    return mapFile

def numberToMString(num: int, binarySize: int) -> str:
    """
    Pre:    num contains the number of bits that were added at the end of the binary compression of a file for 
            alignment purposes and binarySize is the number of bits that we may use to represent num 
    Post:   returns a binarySize-length bit representation string of num
    
    
    Time Complexity:  O(1)
    """  
    
    return bin(num%2**binarySize)[2:].zfill(binarySize)


def getTreeAndDataFromBinary(bits: str):
    """
    Pre:    bits is a string of 0's and 1's with the following structure:
                - header of 3 characters representing the number of characters added 
                at the end of the string
                - 32 characters with the size in bytes of the tree binary representation
                - The binary representation of a GenericTree
                - The compressed file representation
    Post:   Returns the binary string of the compressed file and the GenericTree of the encoding.
    
    Time Complexity: O(m) with m the length of the tree
    """
    
    # Delete alignment header O(m)
    aligned_data = getStringFromBinary(bits)
    
    # Get size of the tree binary representation O(1)
    header_tree_size = int(aligned_data[0:4*8],2)
    
    # Delete size characters O(1)
    aligned_data = aligned_data[4*8:]
    
    # Get a GenericTree from the tree binary representation O(m)
    tree = pickle.loads(BitArray(bin=aligned_data[:header_tree_size*8]).bytes) 

    # Get compressed data O(1)
    rest_data = aligned_data[header_tree_size*8:]
    
    return rest_data, tree

def getStringFromBinary(bits: str) -> str:
    """
    Pre:    bits is a string of 0's and 1's with a header of 3 characters and
            representing the number of characters added at the end of the string
            for alignment purposes.
    Post:   Returns the string deleting the header and the added characters.
    
    
    TimeComplexity: O(1)
    """
    
    num_added = int(bits[0:3],2) # Get number of characters added at the end of the string
    
    # Delete the added characters
    if num_added == 0:
        return bits[3:]
    else:
        return bits[3:-num_added]



def Huffman(file: str) -> GenericTree:
    """
    Pre:    file is the name of a existing file
    Post:   It return a Huffman Generic Tree (see :fun:`my text <mymodule.MyClass.foo>`) with the representation
            of the dictionary of "file".
            
            
    Time Complexity : O(n*m + m*log(m))
    """
    
    queue = []
    map = ParseFile(file) # Time Complexity : O(n*m)

    if len(map) == 0:
        raise Exception("Empty File")
    
    # Initialize the priority queue with one character trees
    # Time Complexity O(m*log(m))
    for key,value in map.items():
        auxTree = GenericTree(key,None,None)
        heapq.heappush(queue,(value,auxTree))
    
    if len(map) == 1 :
        key,value = map.popitem()
        return GenericTree(value,GenericTree(key,None,None),None)
    
    # Joining least priority trees in queue.
    # Time Complexity O(m*log(m))
    for i in range(len(map)-1):
        valueX,treeX = heapq.heappop(queue)
        valueY,treeY = heapq.heappop(queue)
        
        valueZ = valueX+valueY
       
        treeZ = GenericTree(valueZ,treeX,treeY)
        heapq.heappush(queue,(valueZ,treeZ))
    
    # Return the complete tree.
    value,tree = heapq.heappop(queue)
    return tree
