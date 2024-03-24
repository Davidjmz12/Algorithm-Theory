
set title "Recursive vs Dynamic Time-Articles Plot"

set xlabel "Number of articles"
set ylabel "Time in ms"
plot "test/out/iterative/test1.txt" using 1:5 with linespoints title "Dynamic", \
    "test/out/recursive/test1.txt" using 1:5 with linespoints title "Recursive", \
    "test/out/practica_2/test1.txt" using 1:3 with linespoints title "Session 2"


pause -1