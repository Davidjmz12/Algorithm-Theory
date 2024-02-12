##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 3-1-24                                                                                               #
# Subject: Algoritmia básica                                                                                 #
# Description: contains the definition and implementation of all necessary functions to run a time analysis  # 
# of our implementation of Huffman's algorithm                                                               #                       
##############################################################################################################
from typing import List
from huffman import Decode,Encode
import time
from os import mkdir
from sys import argv
from shutil import rmtree

def createFile(size:str, name:str, numChars:int):
    """
    Pre:    numChars <= 126-33
    Post:   creates a size-length text file consisting of printable ASCII
            characters
    """

    with open(name,"w") as file:
        for i in range(size):
            file.write(chr(i%numChars+33))


def createFiles(intArray: List[int], numChars: str, path: str):
    """
    Pre:    intArray contains the range of files to create, numChars <= 126-33,
            path contains the relative path of the file to create
    Post:   creates text files consisting of intArray[i] printable ASCII characters
    """

    for i in intArray:
        name = f"{path}/_{i}"
        createFile(i,name,numChars)
    
    print("Files Created...")
        

def getTimes(timeFile: str, intArray: List[int], numChars: str, path: str):
    """
    Pre:    timeFile contains the relative path of a file in which we capture the 
            time measures taken to run a time analysis of our implementation
    Post:   captures all time measures needed to run a time analysis of our
            implementation
    """

    mkdir(path)
    mkdir(f"{path}/encoded")
    mkdir(f"{path}/decoded")
    createFiles(intArray,numChars,path)
    
    with open(timeFile+"_encode","w") as f:
        f.write(f"#Num Chars: {numChars}\n")
        for i in intArray:
            f.write(f"{i} ")
            name = f"{path}/_{i}"    
            before = time.time()
            Encode(name,f"{path}/encoded/_{i}")
            after = time.time()
            f.write(f"{after-before}\n")
    
    print("Files Encoded...")
    
    with open(timeFile+"_decode","w") as f:
        f.write(f"#Num Chars: {numChars}\n")
        for i in intArray:
            f.write(f"{i} ")
            name = f"{path}/encoded/_{i}"   
            before = time.time()
            Decode(name,f"{path}/decoded/_{i}")
            after = time.time()
            f.write(f"{after-before}\n")

    print("Files Decoded...")

rmtree(argv[6], ignore_errors=True)

if(len(argv) < 7):
    print("Usage: timeFunctions.py <inferior_character_limit> <superior_character_limit> <step> <time_file_name> <number_of_ch∫aracters> <directory_name>")
    exit(-1)


rang = list(range(eval(argv[1]),eval(argv[2]), eval(argv[3])))
getTimes(argv[4],rang, eval(argv[5]), argv[6])

    