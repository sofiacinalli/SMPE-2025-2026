Quicksort

--> Choose a pivot aleatory value and then the system order each value following the condintion: 
    - on the left the values<pivot 
    - on the right the values>pivot 
Parallel quicksort
--> it make the same process as before but with more than one pivot in paralel. 
Built in quicksort
--> use C language to process it. Idem the first one but more optimized

Experiment: Windows 
First time: 
./src/parallelQuicksort 
Sequential quicksort took: 0.207954 sec.
Parallel quicksort took: 0.264888 sec.
Built-in quicksort took: 0.182777 sec.

Second time:
Sequential quicksort took: 0.224824 sec.
Parallel quicksort took: 0.198254 sec.
Built-in quicksort took: 0.171846 sec.

Third time:
Sequential quicksort took: 0.204111 sec.
Parallel quicksort took: 0.254295 sec.
Built-in quicksort took: 0.191175 sec.


Which means that built in is faster than sequential quicksort and parallel. 
There is a variation between sequential and paralel

Having 100 elements: ./src/parallelQuicksort 100
first time
Sequential quicksort took: 0.000014 sec.
Parallel quicksort took: 0.016857 sec.
Built-in quicksort took: 0.000011 sec.
second time
Sequential quicksort took: 0.000018 sec.
Parallel quicksort took: 0.016007 sec.
Built-in quicksort took: 0.000007 sec.
third time
Sequential quicksort took: 0.000013 sec.
Parallel quicksort took: 0.013217 sec.
Built-in quicksort took: 0.000006 sec.

After doing some test, I made the following:
1) Create a code in Python order to have more information: 
Name of the doc: test parallelQuicksort.py

     import subprocess
            x = 0
            matrix_register = []
            
            while x < 3000000:
                result = subprocess.run(
                    ["./src/parallelQuicksort", str(x)], 
                    capture_output = True,
                    text = True
                    )
                matrix_register.append(result.stdout)
                x = x + 300000

2) Choose 1 value for check the resault:
Name of the doc: test parallelQuicksort.py

     import subprocess
            x = 0
            matrix_register = []
            
            while x < 3000000:
                result = subprocess.run(
                    ["./src/parallelQuicksort", str(x)], 
                    capture_output = True,
                    text = True
                    )
                matrix_register.append(result.stdout)
                x = x + 300000
     print (matrix_register[2]) 

3) I process the code in Ubuntu because in python it doesnt function if i work with windows. 

sofic@Sofia:~$ cd /mnt/c/Users/sofic/OneDrive/Documentos/M2R-ParallelQuicksort/M2R-ParallelQuicksort-master
sofic@Sofia:/mnt/c/Users/sofic/OneDrive/Documentos/M2R-ParallelQuicksort/M2R-ParallelQuicksort-master$ code .
sofic@Sofia:/mnt/c/Users/sofic/OneDrive/Documentos/M2R-ParallelQuicksort/M2R-ParallelQuicksort-master$ cd /mnt/c/Users/sofic/OneDrive/Documentos/M2R-ParallelQuicksort/M2R-ParallelQuicksort-master
sofic@Sofia:/mnt/c/Users/sofic/OneDrive/Documentos/M2R-ParallelQuicksort/M2R-ParallelQuicksort-master$ python3 "test parallelQuicksort.py"
Sequential quicksort took: 0.077588 sec.
Parallel quicksort took: 0.141773 sec.
Built-in quicksort took: 0.043563 sec.

4) At that moment I recognize that each value has text and number so it will be a problem when I will try to graph so I modify the code in order to only have the numbers.
import subprocess
x = 0
matrix_register = []

while x < 3000000:
    result = subprocess.run(
        ["./src/parallelQuicksort", str(x)], 
        capture_output = True,
        text = True
        )
    lines = result.stdout.splitlines()
    sequential_time = float(lines[0].split()[3]) #i ONLY save the numeric part from the variable  
    parallel_time   = float(lines[1].split()[3])
    builtin_time    = float(lines[2].split()[3])

    matrix_register.append([x, sequential_time, parallel_time, builtin_time])
    x = x + 300000

print (matrix_register[2]) 

5) Procedure with export the information:
python3 "Test parallelQuicksort.py"
[900000, 0.144466, 0.14656, 0.122316]

6) After that i procedure with the graph, so the complet algorithm is: 
import subprocess
x = 0
matrix_register = []

while x < 3000000:
    result = subprocess.run(
        ["./src/parallelQuicksort", str(x)], 
        capture_output = True,
        text = True
        )
    lines = result.stdout.splitlines()
    sequential_time = float(lines[0].split()[3])
    parallel_time   = float(lines[1].split()[3])
    builtin_time    = float(lines[2].split()[3])

    matrix_register.append([x, sequential_time, parallel_time, builtin_time])
    x = x + 300000

# print (matrix_register[3]) Prueba  realizada para ver funcionamiento

#graph

import matplotlib.pyplot as plt

sizes = [row[0] for row in matrix_register]         # X
sequential = [row[1] for row in matrix_register]    # Y (secuential)
parallel = [row[2] for row in matrix_register]      # Y (paralLel)
builtin = [row[3] for row in matrix_register]       # Y (built-in)

plt.plot(sizes, sequential,color="red",marker="o",label="Sequential")
plt.plot(sizes, parallel,color="green",marker="*",label="Parallel")
plt.plt( sizes, builtin, color="blue", marker="+", label="Built-in")

plt.xlabel("Array size")
plt.ylabel("Time")
plt.title("Comparison of Quicksort times")
plt.grid(True)                      #Cuadrícula 
plt.legend(loc='upper right')       #legend
plt.show()

And the resoult are:
First time: 
<img width="939" height="483" alt="image" src="https://github.com/user-attachments/assets/a452b00b-989e-4f2d-b44f-b960137eab09" />

Second time: 
<img width="1569" height="835" alt="image" src="https://github.com/user-attachments/assets/cf61bb22-08e2-4e42-a2df-fb38f1d8f014" />

Third time: 
<img width="1591" height="809" alt="image" src="https://github.com/user-attachments/assets/34085541-dfcd-400f-a756-c53c258a240d" />




