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

## Question 1: Overall mortality rates by smoking status

For this first question, we begin by reading the dataset and constructing a contingency table in order to analyze the total number of women who were alive or dead after the follow-up period, according to their smoking habits.

The analysis was performed using R. The following code was used to load the data and compute the mortality statistics:

```{r}
tab <- table(data$Smoker, data$Status)
result <- data.frame(
  alive = tab[, "Alive"],
  dead  = tab[, "Dead"]
)
```

# Add mortality ratio
result$ratio_dead_percentage <- round(100* result$dead / (result$dead + result$alive),1)
result

The table below shows the total number of women alive and dead, stratified by smoking status:
<img width="1203" height="148" alt="image" src="https://github.com/user-attachments/assets/c68f9333-6ebd-4d83-9d84-b2fd3bc23291" />

The following graph shows the mortality rate together with the corresponding 95% confidence intervals for each group:
<img width="836" height="524" alt="image" src="https://github.com/user-attachments/assets/def41de7-6605-4288-a999-dd9cc33e0ac7" />

Looking at this previos results, they show a higher mortality rate among non-smokers than among smokers. This result may seem surprising,
However, at this stage, we should be careful with this interpretation. Important factors such as age or other health conditions are not included yet. A deeper analysis is needed before making any conclusions.

## Question 2: Investigate the effect of age.
To do so we are going to create 4 cathegories as shown: 18-34 years, 34-54 years, 55-64 years, over 65 years.
The following code it was created to do that in R:
```{r}
data$age_group <- NA

data$age_group[data$Age >= 18 & data$Age <= 35] <- "18-35"
data$age_group[data$Age > 35  & data$Age <= 54] <- "35-54"
data$age_group[data$Age > 54  & data$Age <= 64] <- "55-64"
data$age_group[data$Age >= 65] <- "65+"

table(data$age_group)
```

Now we are going to analyze the dead ratio for each group:

Table from smoker people: 
<img width="1176" height="180" alt="image" src="https://github.com/user-attachments/assets/75bbe768-2cb6-4dcf-8046-837df6b78958" />

Table from non smoker people:
<img width="1163" height="183" alt="image" src="https://github.com/user-attachments/assets/00c37562-c899-4356-9fd1-760489004c65" />

We also create a bar chart in order to see in a more clear way the results: 
<img width="801" height="468" alt="image" src="https://github.com/user-attachments/assets/69b02a55-45f4-4caf-909f-09ca9614ddbe" />

When the data are analyzed by age group, smokers show a higher mortality rate than non-smokers in each age category. However, when all ages are combined, the overall result suggests the opposite. This change in the relationship after stratifying by age illustrates Simpson’s paradox, where a hidden variable (age) strongly influences the observed outcome.

## Question 3: - Use logistic regression to model mortality as a function of age and smoking status.

The following graph shows Logistic regression of the Probability of Death as a function of Age (95% CI)

<img width="827" height="518" alt="image" src="https://github.com/user-attachments/assets/bab56ede-e62c-4371-be1e-52fc9fccfd92" />

What this graph shows is that the probability of death increases with age for both smokers and non-smokers. For a given age, smokers have a higher probability of death than non-smokers. This indicates that age is a strong confounding variable and explains the paradox observed in the aggregated analysis. By using age as a continuous variable, the model avoids arbitrary age groups and provides clearer evidence of the harmful effect of smoking.

