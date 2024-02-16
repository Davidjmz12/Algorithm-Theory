from os import mkdir
from shutil import rmtree
from sys import argv
from backtracking import backtracking
from article import Article
from variables import Variables
import time

def file_to_variables(file_name):
    
    with open(file_name,"r") as f:
        header = f.readline()
        variables = []
        
        while header:
            header = header[:-1]
            page_list = [int(_) for _ in header.split(" ")]
            page = Article((0,0), page_list[2], page_list[1]).polygon
            n = page_list[0]

            list_art = []
            
            for i in range(0, n):
                line = f.readline()[:-1]
                one_art_l = [int(_) for _ in line.split(" ")]
                list_art.append(Article((one_art_l[2],one_art_l[3]), one_art_l[1], one_art_l[0])) 
            
            variables.append(Variables(list_art,n,page))
            header = f.readline()
    
        return variables

def main():
    
    file1 = "test/in/test0.txt"
    file2 = "test/out/test0.txt"

    variables = file_to_variables(file1)

    with open(file2,"w") as w_f:
        
        rmtree("svg", ignore_errors=True)
        mkdir("svg")
        i=0
        w_f.write("Results from " + file1 + "\n")
        for variable in variables:
            now = time.time()
            size = backtracking(variable)
            time_elapsed = time.time()-now
            w_f.write(f"{size} {time_elapsed}\n")
            variable.write_svg("svg/_"+str(i)+".svg")
            i+=1
        
main()
    