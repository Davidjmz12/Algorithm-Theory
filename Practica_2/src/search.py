##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 24-2-24                                                                                              #
# Subject: Algoritmia básica                                                                                 #
# Description: contains the definition and implementation of functions that give a text file containing the  #
# size of a paper's page and a list of articles with their corresponding origin coordinates and size,        #
# computes the articles that must be chosen in order to use the maximum area of the page possible            #
##############################################################################################################
from os import mkdir
from shutil import rmtree
from sys import argv
from backtracking import backtracking
from variables import file_to_variables
import time


def main():
    file1 = "test/in/test5.txt"
    file2 = "test/out/test5.txt"

    variables = file_to_variables(file1)

    with open(file2, "w") as w_f:
        rmtree("svg", ignore_errors=True)
        mkdir("svg")
        i = 0
        w_f.write("Results from " + file1 + "\n")
        for variable in variables:
            now = time.time()
            size, num_cases = backtracking(variable)
            time_elapsed = (time.time() - now) * 1000
            w_f.write(f"{size} {num_cases} {time_elapsed}\n")
            variable.write_svg("svg/_" + str(i) + ".svg")
            i += 1


main()
