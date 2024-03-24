
set title "Backtracking Time-Articles"

set xlabel "Number of articles"
set ylabel "Time in ms"
plot "test/out/test5.txt" using 1:4 with linespoints title "time"

pause -1