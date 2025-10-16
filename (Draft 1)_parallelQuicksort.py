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

for run in range(1,6):
    data = matrix_quicksort()

    #graph
    sizes = [row[0] for row in data]         # X
    sequential = [row[1] for row in data]    # Y (secuential)
    parallel = [row[2] for row in data]      # Y (paralLel)
    builtin = [row[3] for row in data]       # Y (built-in)

    plt.figure(figsize=(8,5))
    plt.plot(sizes, sequential, color="red", marker="o", label="Sequential")
    plt.plot(sizes, parallel, color="green", marker="*", label="Parallel")
    plt.plot(sizes, builtin, color="blue", marker="+", label="Built-in")

    plt.xlabel("Array size")
    plt.ylabel("Time")
    plt.title("Comparison of Quicksort times")
    plt.grid(True)                      #grid 
    plt.legend(loc='upper right')       #legend
    plt.tight_layout()
    plt.savefig(f"corrida_{run}.png")
    plt.close()
