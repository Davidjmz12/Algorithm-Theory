##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 25-2-24                                                                                              #
# Subject: Algoritmia básica                                                                                 #
# Description: test file to check the correction of our backtracking algorithm                               #
##############################################################################################################

from os import mkdir
from shutil import rmtree
import time,sys

sys.path.append('src')
from variables import file_to_variables
from linearP import linearP
from branch import branch

path_test_in = "test/in/"
path_test_out_branch = "test/out/bound/"
path_test_out_linear_prog = "test/out/lp/"

num_tests = 6
test_files = ["test{}.txt".format(i) for i in range(num_tests)]

test_branch = True
test_linear_prog = True

def test():
    '''
    Test function
    '''
    
    rmtree("test/svg", ignore_errors=True)
    mkdir("test/svg")
    
    for file in test_files:
        
        # Get variables of the file
        variables = file_to_variables(path_test_in + file)
        
        with open(path_test_out_branch + file, "w") as w_branch, open(path_test_out_linear_prog + file, "w") as w_lp:
            
            w_branch.write("Results from " + file + "\n")
            w_lp.write("Results from " + file + "\n")
            
            for i,variable in enumerate(variables):
                
                for fun,w_f,test_it in [(branch,w_branch,test_branch),(linearP,w_lp,test_linear_prog)]:
                    
                    if test_it:                  
                        now = time.time()
                        
                        size, n_branches =  fun(variable)
                        
                        time_elapsed = 1000*(time.time() - now)

                        w_f.write(f"{variable.area_page()-size} {n_branches} {time_elapsed} \n")
                
                variable.write_svg(f"test/svg/_{file}_{i}.svg")

test()
