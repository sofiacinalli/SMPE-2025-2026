import numpy as np
import matplotlib.pyplot as plt
import subprocess
from scipy import stats
from scipy.stats import linregress

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

# run experiments
all_run = []
R=30 #number of runnings
for run in range(R):
    data = matrix_quicksort()
    all_run.append(data)

#graph
sizes = [row[0] for row in data]       
num_registers = len(sizes)


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

#graph means 
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

#COMPUTE 95% CI
# critic value for t para IC 95 %
zcrit = stats.norm.ppf(0.975)   # 0.975 = 95% 

low_seq, high_seq = [], []
low_par, high_par = [], []
low_blt, high_blt = [], []

for i in range(num_registers):
    # Sequential
    seq_vals = np.array([all_run[r][i][1] for r in range(R)])
    sem_seq = np.std(seq_vals, ddof=1) / np.sqrt(R)
    low_seq.append(media_seq[i] - zcrit * sem_seq)
    high_seq.append(media_seq[i] + zcrit * sem_seq)

    # Parallel
    par_vals = np.array([all_run[r][i][2] for r in range(R)])
    sem_par = np.std(par_vals, ddof=1) / np.sqrt(R)
    low_par.append(media_par[i] - zcrit * sem_par)
    high_par.append(media_par[i] + zcrit * sem_par)

    # Built-in
    blt_vals = np.array([all_run[r][i][3] for r in range(R)])
    sem_blt = np.std(blt_vals, ddof=1) / np.sqrt(R)
    low_blt.append(media_built[i] - zcrit * sem_blt)
    high_blt.append(media_built[i] + zcrit * sem_blt)


#dispersion graph in order tu understand the CI
plt.figure(figsize=(9,5))

for i, x in enumerate(sizes):
    # Secuencial
    seq_vals = [all_run[r][i][1] for r in range(R)]
    plt.scatter([x]*R, seq_vals, color="red", alpha=0.3, s=20, label="Sequential" if i == 0 else None)

    # Paralelo
    par_vals = [all_run[r][i][2] for r in range(R)]
    plt.scatter([x]*R, par_vals, color="green", alpha=0.3, s=20, label="Parallel" if i == 0 else None)

    # Built-in
    blt_vals = [all_run[r][i][3] for r in range(R)]
    plt.scatter([x]*R, blt_vals, color="blue", alpha=0.3, s=20, label="Built-in" if i == 0 else None)

plt.xlabel("Array size")
plt.ylabel("Time (s)")
plt.title("Dispersion of runtimes across 30 runs")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("scatter_dispersion.png")
plt.close()

# mean +/- 95% CI
err_seq = np.array(high_seq) - np.array(media_seq)
err_par = np.array(high_par) - np.array(media_par)
err_blt = np.array(high_blt) - np.array(media_built)

plt.figure(figsize=(9,5))

plt.errorbar(sizes, media_seq,   yerr=err_seq, fmt='o-', color="red", capsize=4, label="Sequential (mean ± 95% CI)")
plt.errorbar(sizes, media_par,   yerr=err_par, fmt='o-', color="green",capsize=4, label="Parallel (mean ± 95% CI)")
plt.errorbar(sizes, media_built, yerr=err_blt, fmt='o-', color="blue",capsize=4, label="Built-in (mean ± 95% CI)")

plt.xlabel("Array size")
plt.ylabel("Time (s)")
plt.title("Mean ± 95% CI ")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("test_media_ci95_Z.png")
plt.close()

# Individual plots
plt.figure(figsize=(9,5))
plt.errorbar(sizes, media_seq, yerr=err_seq, fmt='o-', color="red", capsize=4, label="Sequential (mean ± 95% CI)")
plt.xlabel("Array size"); plt.ylabel("Time")
plt.title("Sequential — Mean ± 95% CI (Gaussian Z)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("sequential_media_ci95.png")
plt.close()

plt.figure(figsize=(9,5))
plt.errorbar(sizes, media_par, yerr=err_par, fmt='o-', color="green", capsize=4, label="Parallel (mean ± 95% CI)")
plt.xlabel("Array size"); plt.ylabel("Time")
plt.title("Parallel — Mean ± 95% CI (Gaussian Z)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("parallel_media_ci95.png")
plt.close()

plt.figure(figsize=(9,5))

plt.errorbar(sizes, media_built , yerr=err_blt, fmt='o-', color="blue", capsize=4, label="Built-in (mean ± 95% CI)")
plt.xlabel("Array size"); plt.ylabel("Time")
plt.title("Built-in — Mean ± 95% CI (Gaussian Z)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("BUILTIN_media_ci95.png")
plt.close()

# Linear regression (time vs size)
def plot_linear_regression_scatter(all_run, sizes, algo_col, color_points, title, filename):
    X = []
    Y = []
    for i, x in enumerate(sizes):
        vals = [all_run[r][i][algo_col] for r in range(R)]
        X.extend([x] * len(vals))
        Y.extend(vals)

    X = np.array(X, dtype=float)
    Y = np.array(Y, dtype=float)

    # Linear regression
    res = linregress(X, Y)
    slope = res.slope
    intercept = res.intercept
    r2 = res.rvalue ** 2

    # Prediction line
    x_line = np.linspace(min(sizes), max(sizes), 200)
    y_line = intercept + slope * x_line

    # Plot
    plt.figure(figsize=(8,5))
    plt.scatter(X, Y, color=color_points, alpha=0.6, label="Real times")
    plt.plot(x_line, y_line, color="red", linewidth=2, label="Linear model")

    plt.xlabel("Array size")
    plt.ylabel("Time (s)")
    plt.title(f"{title}\nLinear model: y = {intercept:.2e} + {slope:.2e} x  |  R² = {r2:.3f}")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(loc="best")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

    print(f"{title}:")
    print(f"  slope     = {slope:.6e}")
    print(f"  intercept = {intercept:.6e}")
    print(f"  R^2       = {r2:.4f}\n")


# Sequential
plot_linear_regression_scatter(
    all_run, sizes,
    algo_col=1,
    color_points="royalblue",
    title="Sequential QuickSort",
    filename="regression_sequential_scatter.png"
)

# Parallel
plot_linear_regression_scatter(
    all_run, sizes,
    algo_col=2,
    color_points="forestgreen",
    title="Parallel QuickSort",
    filename="regression_parallel_scatter.png"
)

# Built-in (opcional)
plot_linear_regression_scatter(
    all_run, sizes,
    algo_col=3,
    color_points="darkorange",
    title="Built-in sort",
    filename="regression_builtin_scatter.png"
)
