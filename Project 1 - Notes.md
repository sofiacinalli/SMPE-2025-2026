Quicksort

Choose a pivot aleatory value and then the system order each value following the condintion: 
a. on the left the values<pivot
b. on the right the values>pivot 

Parallel quicksort: it make the same process as before but with more than one pivot in paralel. 
Built in quicksort use C language to process it. Idem the first one but more optimized

Experiment: Windows 
First time: 
./src/parallelQuicksort 
1. Sequential quicksort took: 0.207954 sec.
2. Parallel quicksort took: 0.264888 sec.
3. Built-in quicksort took: 0.182777 sec.

Second time:
1. Sequential quicksort took: 0.224824 sec.
2. Parallel quicksort took: 0.198254 sec.
3. Built-in quicksort took: 0.171846 sec.

Third time:
1. Sequential quicksort took: 0.204111 sec.
2. Parallel quicksort took: 0.254295 sec.
3. Built-in quicksort took: 0.191175 sec.


Which means that built in is faster than sequential quicksort and parallel. 
There is a variation between sequential and paralel

Having 100 elements: ./src/parallelQuicksort 100
first time
1. Sequential quicksort took: 0.000014 sec.
2. Parallel quicksort took: 0.016857 sec.
3. Built-in quicksort took: 0.000011 sec.

second time
1. Sequential quicksort took: 0.000018 sec.
2. Parallel quicksort took: 0.016007 sec.
3. Built-in quicksort took: 0.000007 sec.

third time
1. Sequential quicksort took: 0.000013 sec.
2. Parallel quicksort took: 0.013217 sec.
3. Built-in quicksort took: 0.000006 sec.

Conclusion: for numbers < 100 built-in is more quickly than the others
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

6) After that, in order to procedure with the graph, the complet algorithm is on PROJECT 1 - code: 

And the resoult are:
First time: 
<img width="939" height="483" alt="image" src="https://github.com/user-attachments/assets/a452b00b-989e-4f2d-b44f-b960137eab09" />

Second time: 
<img width="1569" height="835" alt="image" src="https://github.com/user-attachments/assets/cf61bb22-08e2-4e42-a2df-fb38f1d8f014" />

Third time: 
<img width="1591" height="809" alt="image" src="https://github.com/user-attachments/assets/34085541-dfcd-400f-a756-c53c258a240d" />

Seen this graph we can say that is not something stable, but we can say that secuential programing has better behavior than parallel when we analyize less than 1.500.000 of values and sequential has the opposit behavior. In all of the cases, built-in takes less time, so we can say that it is the most optimous for all of the cases. But we cant conclude nothing if we don't have enaugh numbers of demostrations and also it doesent seams to be stable so we procedure with point 7

7)Analyzing that is not something stable, we can create more runs of the process. For example: 5  

<img width="800" height="500" alt="corrida_1" src="https://github.com/user-attachments/assets/eb0a5973-592f-425a-9c5a-f4d7a5d1fda5" />
<img width="800" height="500" alt="corrida_2" src="https://github.com/user-attachments/assets/4b51591e-15f6-433d-8cd6-267f73e0703f" />
<img width="800" height="500" alt="corrida_3" src="https://github.com/user-attachments/assets/6c7b1a7f-bbd8-4c37-92d6-40475bb10a16" />
<img width="800" height="500" alt="corrida_4" src="https://github.com/user-attachments/assets/7459c7f8-321a-439b-bd8e-5e1336283ba8" />
<img width="800" height="500" alt="corrida_5" src="https://github.com/user-attachments/assets/22cc149e-a680-4d25-96f8-c9a3f428d453" />





