# JTSK-350112
# plotting.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

import subprocess

# print x and x^2 to a file square.dat
file = open("square.dat", "w")
i = -5
while i <= 5:
    file.write("{} {}\n".format(i, i ** 2))
    i += 0.1

file.close()

# plot the data using gnuplot. The interval is [-5; 5]
proc = subprocess.Popen(['gnuplot'], shell = True, stdin=subprocess.PIPE)
proc.stdin.write(b'set terminal png\n')
proc.stdin.write(b'set output "result.png"\n')
proc.stdin.write(b'set title "Plotting"\n')
proc.stdin.write(b'set grid\n')
proc.stdin.write(b'set xrange [-5:5]\n')
proc.stdin.write(b'set yrange [-5:5]\n')
proc.stdin.write(b'plot "square.dat" using 1:1 with lines, "square.dat" using 1:2 with lines')