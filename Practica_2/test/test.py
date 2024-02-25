##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 25-2-24                                                                                               #
# Subject: Algoritmia básica                                                                                 #
# Description: test file to check the correction of our backtracking algorithm                               #                                                                                   #                        
##############################################################################################################

from os import mkdir
from shutil import rmtree
import sys
import time

sys.path.append('src')
from search import file_to_variables
from backtracking import backtracking

path_test_in = "test/in/"
path_test_out = "test/out/"

num_tests = 5
test_files = ["test{}.txt".format(i) for i in range(num_tests)]


def test():
    rmtree("svg", ignore_errors=True)
    mkdir("svg")
    for file in test_files:
        variables = file_to_variables(path_test_in+file)
        with open(path_test_out+file, "w") as w_f:
            i=0
            w_f.write("Results from " + file + "\n")
            for variable in variables:
                now = time.time()
                size, num_cases = backtracking(variable)
                time_elapsed = time.time()-now
                w_f.write(f"{size} {num_cases} {time_elapsed}\n")
                variable.write_svg("svg/_"+file+"_"+str(i)+".svg")
                i+=1


test()