
set title "Comparision different algorithms"

set xlabel "Number of articles"
set ylabel "Time in ms"
plot "test/out/iterative/test1.txt" using 1:3 with linespoints title "Dynamic", \
    "test/out/recursive/test1.txt" using 1:3 with linespoints title "Recursive", \
    "test/out/practica_2/test1.txt" using 1:3 with linespoints title "Prune", \
    "test/out/greedy/test1.txt" using  1:3 with linespoints title "Greedy"
pause -1