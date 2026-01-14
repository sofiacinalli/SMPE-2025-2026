# Subject 6: Around Simpson's Paradox

## Overview
In this work, we analyze the results of a survey conducted in Whickham, a town in the north-east of England located approximately 6.5 kilometres south-west of Newcastle upon Tyne.  
The objective of the original study was to investigate thyroid and heart disease.

The survey was conducted in two periods:
- an initial study carried out between 1972 and 1974 to collect baseline information,
- a follow-up study conducted approximately 20 years later to assess the health status of the participants.

This project focuses on the relationship between smoking habits, age, and mortality, and illustrates the well-known **Simpson's Paradox**.

## Dataset
The dataset contains information about women from the Whickham study who were classified as *current smokers* or *never smokers* at the time of the first survey.

For each individual, the following variables are available:
- **Smoking status**: smoker / non-smoker 
- **Vital status**: alive / dead at follow-up
- **Age**: age at the time of the first survey

## Tools
- **R** (RStudio)

## Objectives:
The objective of this project is to do the following questions: 
1. Tabulate the total number of women alive and dead over the period according to their smoking habits. Calculate in each group (smoking/non-smoking) the mortality rate (the ratio of the number of women who died in a group to the total number of women in that group). You can graph these data and calculate confidence intervals if you wish. Why is this result surprising?

2. Go back to question 1 (numbers and mortality rates) and add a new category related to the age group. For example, the following classes will be considered: 18-34 years, 34-54 years, 55-64 years, over 65 years.
Why is this result surprising? Can you explain this paradox? Similarly, you may wish to provide a graphical representation of the data to support your explanations.

3. In order to avoid a bias induced by arbitrary and non-regular age groupings, it is possible to try to perform a logistic regression. If we introduce a Death variable of 1 or 0 to indicate whether the individual died during the 20-year period, we can study the Death ~ Age model to study the probability of death as a function of age according to whether one considers the group of smokers or non-smokers. Do these regressions allow you to conclude or not on the harmfulness of smoking? You will be able to propose a graphical representation of these regressions (without omitting the regions of confidence).

## Objectives
- Compute overall mortality rates by smoking status
- Investigate the effect of age as a confounding variable
- Illustrate Simpson's Paradox through stratified analysis
- Use logistic regression to model mortality as a function of age and smoking status

## Question 1: Overall mortality rates by smoking status

For this first question, we begin by reading the dataset and constructing a contingency table in order to analyze the total number of women who were alive or dead after the follow-up period, according to their smoking habits.

The analysis was performed using R. The following code was used to load the data and compute the table:

```r
data <- read.csv("Subject6_smoking.csv")

table(data$Smoker, data$Status)
