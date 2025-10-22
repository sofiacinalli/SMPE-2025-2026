import subprocess
import matplotlib.pyplot as plt

def matrix_quicksort():
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
    return matrix_register

all_run = []
R=30 #number of runnings
for run in range(R):
    data = matrix_quicksort()
    all_run.append(data)

    #graph
    sizes = [row[0] for row in data]         # X
    sequential = [row[1] for row in data]    # Y (secuential)
    parallel = [row[2] for row in data]      # Y (paralLel)
    builtin = [row[3] for row in data]       # Y (built-in)

#    plt.figure(figsize=(8,5))
#    plt.plot(sizes, sequential, color="red", marker="o", label="Sequential")
#    plt.plot(sizes, parallel, color="green", marker="*", label="Parallel")
#    plt.plot(sizes, builtin, color="blue", marker="+", label="Built-in")
#
#   plt.xlabel("Array size")
#   plt.ylabel("Time")
#    plt.title("Comparison of Quicksort times")
#    plt.grid(True)                      #grid 
#    plt.legend(loc='upper right')       #legend
#    plt.tight_layout()
#    plt.savefig(f"corrida_{run}.png")
#    plt.close()

import numpy as np

media_seq = []
media_par = []
media_built = []

for i in range(10):  #10 because of the increment 300.000 and <3.000.000
    values_seq = np.array([all_run[r][i][1] for r in range(R)])   #R the number of runs
    prom_seq = np.mean(values_seq) 
    media_seq.append(prom_seq)  
    
    values_par = np.array([all_run[r][i][2] for r in range(R)])   #R the number of runs
    prom_par = np.mean(values_par) 
    media_par.append(prom_par)  

    values_built = np.array([all_run[r][i][3] for r in range(R)])   #R the number of runs
    prom_built = np.mean(values_built) 
    media_built.append(prom_built)  

#graph media
sizes = [row[0] for row in all_run[0]]         # X
sequential_media = media_seq   
parallel_media = media_par    
builtin_media = media_built       

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

from scipy import stats

# ---COMPUTE CI 95 % ---
num_registers = len(all_run[0])

# save low values and high values
low_seq, high_seq = [], []
low_par, high_par = [], []
low_blt, high_blt = [], []

# critic value for t para IC 95 %
tcrit = stats.t.ppf(0.975, df=R-1)   # 0.975 = 95% 

for i in range(num_registers):
    # --- Sequential ---
    seq_vals = np.array([all_run[r][i][1] for r in range(R)])
    sem_seq = np.std(seq_vals, ddof=1) / np.sqrt(R)
    low_seq.append(media_seq[i] - tcrit * sem_seq)
    high_seq.append(media_seq[i] + tcrit * sem_seq)

    # --- Parallel ---
    par_vals = np.array([all_run[r][i][2] for r in range(R)])
    sem_par = np.std(par_vals, ddof=1) / np.sqrt(R)
    low_par.append(media_par[i] - tcrit * sem_par)
    high_par.append(media_par[i] + tcrit * sem_par)

    # --- Built-in ---
    blt_vals = np.array([all_run[r][i][3] for r in range(R)])
    sem_blt = np.std(blt_vals, ddof=1) / np.sqrt(R)
    low_blt.append(media_built[i] - tcrit * sem_blt)
    high_blt.append(media_built[i] + tcrit * sem_blt)


plt.figure(figsize=(9,5))

# # Average
plt.plot(sizes, media_seq, color="red",   marker="o", label="Sequential (mean)")
plt.plot(sizes, media_par, color="green", marker="o", label="Parallel (mean)")
plt.plot(sizes, media_built, color="blue",  marker="o", label="Built-in (mean)")

# CI 95% - TSTUDENT
plt.fill_between(sizes, low_seq, high_seq, color="red", alpha=0.15, label="Seq 95% CI")
plt.fill_between(sizes, low_par, high_par, color="green", alpha=0.15, label="Par 95% CI")
plt.fill_between(sizes, low_blt, high_blt, color="blue", alpha=0.15, label="Built-in 95% CI")

plt.xlabel("Array size")
plt.ylabel("Time (s)")
plt.title("Quicksort — Mean ± 95% CI")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("test_media_ci95.png")
plt.close()

#sequential PLOT
plt.figure(figsize=(9,5))

# Average
plt.plot(sizes, media_seq, color="red",   marker="o", label="Sequential (mean)")

# CI 95%
plt.fill_between(sizes, low_seq, high_seq, color="red", alpha=0.15, label="Seq 95% CI")

plt.xlabel("Array size")
plt.ylabel("Time (s)")
plt.title("Quicksort — Mean ± 95% CI")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("sequential_media_ci95.png")
plt.close()

#PARALLEL PLOT
plt.figure(figsize=(9,5))

# # Average
plt.plot(sizes, media_par, color="green", marker="o", label="Parallel (mean)")

# CI 95% - TSTUDENT
plt.fill_between(sizes, low_par, high_par, color="green", alpha=0.15, label="Par 95% CI")

plt.xlabel("Array size")
plt.ylabel("Time (s)")
plt.title("Quicksort — Mean ± 95% CI")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("parallel_media_ci95.png")
plt.close()

#built_in plot
plt.figure(figsize=(9,5))

# # Average

plt.plot(sizes, media_built, color="blue",  marker="o", label="Built-in (mean)")

# CI 95% - TSTUDENT
plt.fill_between(sizes, low_blt, high_blt, color="blue", alpha=0.15, label="Built-in 95% CI")

plt.xlabel("Array size")
plt.ylabel("Time (s)")
plt.title("Quicksort — Mean ± 95% CI")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("BUILTIN_media_ci95.png")
plt.close()
