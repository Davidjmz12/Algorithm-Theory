##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 3-1-24                                                                                               #
# Subject: Algoritmia básica                                                                                 #
# Description: test file to check the correction of our Huffman algorithm implementation                     #                                                                                   #                        
##############################################################################################################
from os import mkdir
from shutil import rmtree

import sys

sys.path.append('src/huffman')
from huffman import Encode, Decode

path_test = "tests/"
path_test_files = path_test + "test_files/"
path_encode_files = path_test + "encode/"
path_decode_files = path_test + "decode/"

num_tests = 5
test_files = ["test{}.txt".format(i) for i in range(num_tests)]

def compare(file: str, decodedFileName: str) -> bool:
    with open(file, 'r') as original_file, open(decodedFileName, 'r') as decoded_file:           
        return decoded_file.read() == original_file.read()

def test():
    
    rmtree(path_decode_files,ignore_errors=True)
    rmtree(path_encode_files, ignore_errors=True)

    mkdir(path_decode_files)
    mkdir(path_encode_files)
    
    for file in test_files:
        encodedFileName = path_encode_files + file + ".huf"
        if(Encode(path_test_files + file, encodedFileName)) != -1:
            decodedFileName = path_decode_files + file + ".dec"
            Decode(encodedFileName, decodedFileName) 
            if compare(path_test_files + file, decodedFileName):
                print("File " + path_test_files + file + " encoded and decoded successfully.")
            else:
                print("Decoded file content does not match original content on file: " + path_test_files + file + ".")
    
test()