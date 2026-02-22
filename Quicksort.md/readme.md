# Parallel Quicksort – Experimental Analysis (SMPE 2025–2026)

This project studies and compares the performance of three sorting implementations:

- Sequential Quicksort  
- Parallel Quicksort  
- Built-in sort (C/C++ standard implementation)

The goal is to analyze execution times, variability across runs, confidence intervals.

---

## Repository Structure

The repository contains three main files:
├── Final_code_Quicksort.py # Final experimental script (data collection, plots, CI, regression)
├── Report.md # Final report with analysis, figures and conclusions
└── Code Quicksort.py # Initial version of the Python script (first experiments)

---

## How to Run the Experiments

### Requirements

- Linux / WSL (Ubuntu recommended)  
- Python 3  
- The compiled executable:

Output

The script produces several figures, including:
- Comparison of mean execution times
- Dispersion of runtimes across runs
- Mean ± 95% confidence intervals
- Linear regression with scatter of real measurements
