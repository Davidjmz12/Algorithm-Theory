##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 25-2-24                                                                                              #
# Subject: Algoritmia básica                                                                                 #
# Description: test file to check the correction of our backtracking algorithm                               #
##############################################################################################################

from os import mkdir
from shutil import rmtree
import sys
import time

sys.path.append('src')
from variables import file_to_variables
from recursive import recursive
from iterative import iterative
from greedy import greedy

path_test_in = "test/in/"
path_test_out_iterative = "test/out/iterative/"
path_test_out_recursive = "test/out/recursive/"
path_test_out_greedy = "test/out/greedy/"

num_tests = 3
test_files = ["test{}.txt".format(i) for i in range(num_tests)]

test_recursive = True
test_iterative = True
test_greedy = True

test_to_plot = False


def test(if_recursive,if_iterative,if_greedy):
    '''
    Test function
    '''
    
    rmtree("test/svg", ignore_errors=True)
    mkdir("test/svg")
    
    for file in test_files:
        
        # Get variables of the file
        variables = file_to_variables(path_test_in + file)
        
        with open(path_test_out_iterative + file, "w") as w_iter, open(path_test_out_recursive + file, "w") as w_recur, open(path_test_out_greedy+file, "w") as w_greed:
            
            w_iter.write("Results from " + file + "\n")
            w_recur.write("Results from " + file + "\n")
            w_greed.write("Results from " + file + "\n")
            
            for i,variable in enumerate(variables):
                
                for fun,w_f,iff in [(recursive,w_recur,if_recursive),(iterative,w_iter,if_iterative),(greedy,w_greed,if_greedy)]:
                    
                    if iff:                  
                        now = time.time()
                        
                        size, str_art =  fun(variable)
                        
                        time_elapsed = 1000*(time.time() - now)
                        
                        if test_to_plot:
                            w_f.write(f"{variable.n} {size} {time_elapsed}\n")
                        else:
                            w_f.write(f"{size} {time_elapsed}\n{str_art}")
                
                variable.write_svg(f"test/svg/_{file}_{i}.svg")

test(if_recursive=test_recursive,if_iterative=test_iterative,if_greedy=test_greedy)
