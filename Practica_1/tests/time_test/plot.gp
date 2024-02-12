#  Gnuplot script to get a plot of the times
#  Usage: gnuplot -e "fileEncode='<fileEncode>' ; fileDecode='<fileDecode>" plot.gp

if (!exists("fileEncode")) print "Usage: gnuplot -e \"fileEncode='<fileEncode>' ; filedEcode='<fileDecode>'\"  plot.gp " ;exit
if (!exists("fileDecode")) print "Usage: gnuplot -e \"fileEncode='<fileEncode>' ; fileDecode='<fileDecode>'\"  plot.gp " ;exit

# Set the title using k
set title "Huffman Algorithm times"

# Set axis labels
set xlabel "Length of File(num char)"
set ylabel "Time(ms)"

# Plot the data
plot fileEncode using 1:2 with linespoints title "Encode Time", \
     fileDecode using 1:2 with linespoints title "Decode Time"

pause -1