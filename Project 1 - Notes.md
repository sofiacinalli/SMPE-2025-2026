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

7)Analyzing that is not something stable, we can create more runs of the process. For example: 5  (change the algorithm (Test parallelQuicksort.py) in order to generate the graphs)
<img width="800" height="500" alt="corrida_1" src="https://github.com/user-attachments/assets/5021fc21-c8c8-4b38-8c0e-ca639210bef3" />
<img width="800" height="500" alt="corrida_2" src="https://github.com/user-attachments/assets/8be76b03-4063-4f2d-bb22-42985c5f04cf" />
<img width="800" height="500" alt="corrida_3" src="https://github.com/user-attachments/assets/5a2cea17-a814-47a3-8d0b-d7036a17f280" />
<img width="800" height="500" alt="corrida_4" src="https://github.com/user-attachments/assets/ac7cb25f-57b6-40be-ba36-b11eb5865b7a" />
<img width="800" height="500" alt="corrida_5" src="https://github.com/user-attachments/assets/2638bef2-9bd9-4215-bf6f-2522a3d22f92" />

8) Until now the code only print the information of the 5 runs but it isn't stored so it is necesary to add inside the for the following sentences:
 all_run = []    # in order to declarate the matrix
for run in range(1,6):
    data = matrix_quicksort()
    all_run.append(data)   #in order to stored the 3 values generated in each run

This is with the idea of generate a media between the 5 values and then plot it. So que add this to the code: 

import numpy as np
media_seq = []

for i in range(10):  #10 because of the increment 300.000 and <3.000.000
    values_seq = np.array([all_run[r][i][1] for r in range(5)])   #5 the number of runs
    media_seq = np.mean(valores_seq) 
    medias_seq.append(media_seq)  

For graph: 
for i in range(10):  #10 because of the increment 300.000 and <3.000.000
    values_seq = np.array([all_run[r][i][1] for r in range(5)])   #5 the number of runs
    prom_seq = np.mean(values_seq) 
    media_seq.append(prom_seq)  
    
    values_par = np.array([all_run[r][i][2] for r in range(5)])  
    prom_par = np.mean(values_par) 
    media_par.append(prom_par)  

    values_built = np.array([all_run[r][i][3] for r in range(5)])   
    prom_built = np.mean(values_built) 
    media_built.append(prom_built)  

#graph media
sizes = [row[0] for row in all_run[0]]        

plt.figure(figsize=(8,5))
plt.plot(sizes, media_seq, color="red", marker="o", label="Sequential")
plt.plot(sizes, media_par, color="green", marker="*", label="Parallel")
plt.plot(sizes,media_built, color="blue", marker="+", label="Built-in")

plt.xlabel("Array size")
plt.ylabel("Time")
plt.title("Comparison of Quicksort times")
plt.grid(True)                      #grid 
plt.legend(loc='upper right')       #legend
plt.tight_layout()
plt.savefig("test_media.png")
plt.close()

*The graph of the media with 5 iterations:

<img width="800" height="500" alt="test_media" src="https://github.com/user-attachments/assets/16e9df40-cfdf-49b7-b0a5-32ffb09354d6" />

9. Having only 5 iterations is not sufficient to make a prediction so lets try to run it 30 times. And the graph of the media is the following:
<img width="800" height="500" alt="test_media" src="https://github.com/user-attachments/assets/ed2f4101-933e-46f7-be93-31a4adbd82ce" />


10. Then we analize the confidence interval and we have the followings graphs: (we analized the CI with the T-STUDENT distribution because we don't know the real distribution of the function neither the number of iterations is not so hi). The confidence that we use is 95%
<img width="900" height="500" alt="test_media_ci95" src="https://github.com/user-attachments/assets/76659284-a15b-4a15-9710-d18312956752" />

<img width="900" height="500" alt="BUILTIN_media_ci95" src="https://github.com/user-attachments/assets/7611f8bc-5173-41ee-9429-54fbe72dc8b5" />
<img width="900" height="500" alt="sequential_media_ci95" src="https://github.com/user-attachments/assets/8e0188d3-08af-4638-8a8c-3c83d580e61e" />
<img width="900" height="500" alt="parallel_media_ci95" src="https://github.com/user-attachments/assets/07886ab9-9c09-4ad6-9196-ae059dabd7d9" />

Conclusion: 
- Using the built-in C implementation is the most efficient option for processing datasets of approximately 1.8 million elements or fewer. For larger datasets, the parallel version outperforms the built-in one. Further analysis is needed to understand whether this trend continues for even larger inputs.
-  The sequential implementation performs better than the parallel one for datasets smaller than 600,000 elements. Beyond this point, the parallel algorithm becomes faster, while the sequential version’s runtime increases more sharply.



