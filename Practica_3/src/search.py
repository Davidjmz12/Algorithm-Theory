##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 24-03-24                                                                                             #
# Subject: Algoritmia básica                                                                                 #
# Description: contains the definition and implementation of functions that given a text file containing the #
# size of a paper's page and a list of articles with their corresponding origin coordinates and size,        #
# computes the articles that must be chosen in order to use the maximum area of the page possible            #
##############################################################################################################

from os import mkdir
from shutil import rmtree
from sys import argv
from recursive import recursive
from iterative import iterative
from variables import file_to_variables
import time


def main(opt,file1,file2):
    
    variables = file_to_variables(file1)

    with open(file2,"w") as w_f:
        
        rmtree("svg", ignore_errors=True)
        mkdir("svg")

        w_f.write("Results from " + file1 + "\n")
        for i,variable in enumerate(variables):
            now = time.time()
            
            function = recursive if opt=="-r" else iterative
            
            size, str_art =  function(variable)
            
            time_elapsed = 1000*(time.time() - now)
            
            w_f.write(f"{size} {time_elapsed} \n {str_art} \n")
            variable.write_svg("svg/_"+str(i)+".svg")
        
main(argv[1],argv[2],argv[3])
    