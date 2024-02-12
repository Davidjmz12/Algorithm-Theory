##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 3-1-24                                                                                               #
# Subject: Algoritmia básica                                                                                 #
# Description: contains the definition and implementation of all necessary functions to develop  Huffman's   #
# compression and decompression algorithm                                                                    #                        
##############################################################################################################
from bitArray import BitArray
from auxiliaryFunctions import *

def Encode(inputFile: str, outputFile: str):
    """
    Pre:   inputFile contains the name of the file we want to compress and outputFile contains the name of the file, once 
           once it's been compressed 
    Post:  compresses the file named inputFile in a file named outputFile 
    
    Time Complexity:  O(n*m+m*log(m))  where n is the length of the file and m is the number of characters
    
    """    

    try:
        tree = Huffman(inputFile)
    except:
        print("Empty File. Nothing to compress")
        return -1

    hashMap = tree.treeToHash()
    
    encode_string = getEncodedString(inputFile, hashMap)
    tree_string = getBinaryStringFromTree(tree)
    numberToFill = 8-(len(encode_string)+3)%8 
    header_string = numberToMString(numberToFill,3)
    
    with open(outputFile,"wb") as f_output:
        bits = BitArray(bin=header_string+tree_string+encode_string+numberToFill*"0")
        bits.tofile(f_output)

def Decode(inputFile: str, outputFile: str):
    """
    Pre:   inputFile contains the name of the file we want to decompress and outputFile contains the name of the file, once 
           once it's been decompressed 
    Post:  decompresses the file named inputFile in a file named outputFile 
    
    
    Time Complexity: O(n + m) where n is the length of the file and m is the number of characters
    
    """
    
    with open(inputFile, 'rb') as binaryInputFile:
        bits = BitArray(bytes=binaryInputFile.read()).bin
        bitsNoHeader,tree = getTreeAndDataFromBinary(bits)
        result = tree.decodeString(bitsNoHeader)
        
    with open(outputFile,"w") as binaryOutput:
        binaryOutput.write(result)