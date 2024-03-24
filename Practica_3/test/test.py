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
from variables import file_to_variables
from recursive import recursive
from iterative import iterative

path_test_in = "test/in/"
path_test_out_iterative = "test/out/iterative/"
path_test_out_recursive = "test/out/recursive/"

num_tests = 3
test_files = ["test{}.txt".format(i) for i in range(2,num_tests)]


def test(if_recursive,if_iterative):
    
    rmtree("test/svg", ignore_errors=True)
    mkdir("test/svg")
    
    for file in test_files:
        
        variables = file_to_variables(path_test_in + file)
        with open(path_test_out_iterative + file, "w") as w_iter, open(path_test_out_recursive + file, "w") as w_recur:
            
            w_iter.write("Results from " + file + "\n")
            w_recur.write("Results from " + file + "\n")
            
            for i,variable in enumerate(variables):
                
                for fun,w_f,iff in [(recursive,w_recur,if_recursive),(iterative,w_iter,if_iterative)]:
                    
                    if iff:                  
                        now = time.time()
                        
                        size, num_art, num_cases =  fun(variable)
                        
                        time_elapsed = 1000*(time.time() - now)
                        
                        w_f.write(f"{variable.n} {size} {num_cases} {num_art} {time_elapsed}\n")
                
                variable.write_svg(f"svg/_{file}_{i}.svg")
            
test(if_recursive=True,if_iterative=True)
