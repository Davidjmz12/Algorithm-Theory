
set title "Comparision different algorithms"

set xlabel "Number of articles"
set ylabel "Time in ms"
plot "test/out/otherAlgorithms/test1_iter.txt" using 1:3 with linespoints title "Dynamic", \
    "test/out/otherAlgorithms/test1_rec.txt" using 1:3 with linespoints title "Recursive", \
    "test/out/otherAlgorithms/test1_p2.txt" using 1:3 with linespoints title "Prune", \
    "test/out/otherAlgorithms/test1_greedy.txt" using  1:3 with linespoints title "Greedy", \
    "test/out/bound/test1.txt" using 2:4 with linespoints title "BranchBound", \
    "test/out/lp/test1.txt" using 2:4 with linespoints title "LinearProg"
pause -1