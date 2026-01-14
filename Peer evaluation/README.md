# Subject 6: Around Simpson's Paradox
This repository contains the analysis of the Whickham survey data, focusing on the relationship between smoking, age, and mortality.  
The project illustrates **Simpson’s Paradox** using descriptive statistics, stratified analysis by age, and logistic regression.

## Repository structure
- `/data_smoking.csv`: dataset used in the analysis
- `Simpson_paradox.Rmd/`: R Markdown file containing the full analysis, code, and visualizations.
- `report_Around_Simpson's_Paradox/`: analysis and visualizations with figures and results

## Analysis overview

The analysis is organized in three main steps:
1. **Overall mortality comparison**  
   Mortality rates are computed for smokers and non-smokers without considering age.  
   This initial analysis leads to a surprising result.
2. **Stratification by age groups**  
   Mortality rates are recalculated within age categories.  
   This reveals a reversal of the relationship and illustrates Simpson’s Paradox.
3. **Logistic regression analysis**  
   A logistic regression model is used to study the probability of death as a continuous function of age, separately for smokers and non-smokers.  

## How to run
1. Clone this repository
2. Open the project in RStudio
3. Install the required packages
4. Open and run `Simpson_paradox.Rmd`

## Requirements
- R
- RStudio
