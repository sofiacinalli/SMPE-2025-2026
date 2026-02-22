# Parallel Quicksort – Experimental Analysis (SMPE 2025–2026)

This project studies and compares the performance of three sorting implementations:

- Sequential Quicksort  
- Parallel Quicksort  
- Built-in sort (C/C++ standard implementation)

The goal is to analyze execution times, variability across runs, confidence intervals.

---

## Repository Structure

- **Final_code_Quicksort.py**: Python script containing the final experimental setup, data collection, confidence interval computation, and visualization of results.  
- **Report.md**: Final report with methodology, figures, analysis of results, and conclusions.  
- **Code Quicksort.py**: Initial version of the Python script used in the first experiments (kept for reference).

---
## Output

The script produces several figures, including:
- Comparison of mean execution times
- Dispersion of runtimes across runs
- Mean ± 95% confidence intervals
- Linear regression with scatter of real measurements

---

## How to Run the Experiments

- Clone this repository  
- Make sure the executable `./src/parallelQuicksort` is compiled  
- Run the final experiment script:

```bash
python3 Final_code_Quicksort.py
