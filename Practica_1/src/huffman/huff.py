## --------------------------------------------------------------------
##                          MAIN    
## --------------------------------------------------------------------

from huffman import Decode,Encode
from sys import argv

code = argv[1]
fileName = argv[2]
if code == "-c":
    Encode(fileName, fileName+".huf")
else:
    Decode(fileName, fileName[:-4])