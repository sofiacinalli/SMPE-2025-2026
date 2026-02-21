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
All computations and plots are generated using R. The full code is available in the notebook. ( https://github.com/sofiacinalli/SMPE-2025-2026/blob/5ae1d9e55d877d601323327409feb0960dd98d36/Peer%20evaluation/Simpson_paradox.Rmd )

## Objectives:
The objective of this project is to do the following questions: 
1. Tabulate the total number of women alive and dead over the period according to their smoking habits. Calculate in each group (smoking/non-smoking) the mortality rate (the ratio of the number of women who died in a group to the total number of women in that group). You can graph these data and calculate confidence intervals if you wish. Why is this result surprising?

2. Go back to question 1 (numbers and mortality rates) and add a new category related to the age group. For example, the following classes will be considered: 18-34 years, 34-54 years, 55-64 years, over 65 years.
Why is this result surprising? Can you explain this paradox? Similarly, you may wish to provide a graphical representation of the data to support your explanations.

3. In order to avoid a bias induced by arbitrary and non-regular age groupings, it is possible to try to perform a logistic regression. If we introduce a Death variable of 1 or 0 to indicate whether the individual died during the 20-year period, we can study the Death ~ Age model to study the probability of death as a function of age according to whether one considers the group of smokers or non-smokers. Do these regressions allow you to conclude or not on the harmfulness of smoking? You will be able to propose a graphical representation of these regressions (without omitting the regions of confidence).

## Question 1: Overall mortality rates by smoking status

For this first question, we begin by reading the dataset and constructing a contingency table in order to analyze the total number of women who were alive or dead after the follow-up period, according to their smoking habits.

We start by computing the overall mortality rates by smoking status in order to obtain a first, aggregated view of the relationship between smoking and mortality.

This first analysis provides an aggregated and descriptive view of the data. At this stage, no confounding variables (such as age) are taken into account, so the results must be interpreted with caution.

```{r}
tab <- table(data$Smoker, data$Status)

result <- data.frame(
  alive = tab[, "Alive"],
  dead  = tab[, "Dead"]
)

# Mortality rate (%)
result$ratio_dead <- round(100 * result$dead / (result$dead + result$alive), 1)

result
```

The output of the previous code is the following table: with the number of women alive and dead, stratified by smoking status:
<img width="1203" height="148" alt="image" src="https://github.com/user-attachments/assets/c68f9333-6ebd-4d83-9d84-b2fd3bc23291" />

To quantify uncertainty, we compute 95% confidence intervals for the mortality rates. 
This is justified because, for large sample sizes, the distribution of the estimated proportions can be approximated by a normal distribution according to the Central Limit Theorem. The standard errors are therefore used to quantify the uncertainty of the mortality rate estimates.

```{r}
result$ci_lower <- result$p_dead - 1.96 * result$se
result$ci_upper <- result$p_dead + 1.96 * result$se

# Convert CI to percentage for plotting
result$ci_lower_pct <- 100 * result$ci_lower
result$ci_upper_pct <- 100 * result$ci_upper

result
```

The following plot shows the mortality rate together with the corresponding 95% confidence intervals for each group:

<img width="836" height="524" alt="image" src="https://github.com/user-attachments/assets/def41de7-6605-4288-a999-dd9cc33e0ac7" />

### Interpretation
Looking at this previos results, they show a higher mortality rate among non-smokers than among smokers. This result may seem surprising.
However, at this stage, we should be careful with this interpretation. Important factors such as age or other health conditions are not included yet. A deeper analysis is needed before making any conclusions.

## Question 2: Investigate the effect of age.
To study the role of age, we create 4 cathegories as shown:
- 18–34 years
- 34–54 years
- 55–64 years
- 65 years and older

This stratification allows us to control for age in a simple way and to observe how mortality rates vary within each age group.

```{r}
data$age_group <- NA

data$age_group[data$Age >= 18 & data$Age <= 35] <- "18-35"
data$age_group[data$Age > 35  & data$Age <= 54] <- "35-54"
data$age_group[data$Age > 54  & data$Age <= 64] <- "55-64"
data$age_group[data$Age >= 65] <- "65+"

table(data$age_group)
```

After creating these age groups, mortality rates are computed separately for smokers and non-smokers within each age category.

Table that combines if the people are still alive or not vs age range TABLE smokers
```{r}
tab_yes <- table(
  data$age_group[data$Smoker == "Yes"],
  data$Status[data$Smoker == "Yes"]
)

table_smokers <- data.frame(
  edad = rownames(tab_yes),
  alive = tab_yes[, "Alive"],
  no_alive = tab_yes[, "Dead"]
)

table_smokers$ratio_dead <- round(
  100 * table_smokers$no_alive / (table_smokers$alive + table_smokers$no_alive),
  1
)

table_smokers
```
Output for smokers: 
<img width="1176" height="180" alt="image" src="https://github.com/user-attachments/assets/75bbe768-2cb6-4dcf-8046-837df6b78958" />

Table no smokers
```{r}
tab_no <- table(
  data$age_group[data$Smoker == "No"],
  data$Status[data$Smoker == "No"]
)

table_nonsmokers <- data.frame(
  edad = rownames(tab_no),
  alive = tab_no[, "Alive"],
  no_alive = tab_no[, "Dead"]
)

table_nonsmokers$ratio_dead <- round(
  100 * table_nonsmokers$no_alive / (table_nonsmokers$alive + table_nonsmokers$no_alive),
  1
)

table_nonsmokers
```

The corresponding table for non-smokers is shown below:
<img width="1145" height="169" alt="image" src="https://github.com/user-attachments/assets/2ca1b68a-c76a-439c-8405-5bf8b75dc6ac" />

Table for graph to compare ratio_dead 
```{r}

age_order <- c("18-35", "35-54", "55-64", "65+")

# Reorder rows to match age_order
smk <- table_smokers[match(age_order, table_smokers$edad), ]
nsmk <- table_nonsmokers[match(age_order, table_nonsmokers$edad), ]

# Create the matrix of dead ratios (%)
ratio_mat <- cbind(
  `Non-smokers` = nsmk$ratio_dead,
  `Smokers`     = smk$ratio_dead
)

rownames(ratio_mat) <- age_order

ratio_mat
```
To make the comparison clearer, a grouped bar chart is also used:
```{r}
# Colors for age groups (same color for smokers and non-smokers)
age_colors <- c("darkgreen", "goldenrod", "orange", "red")

bp <- barplot(
  height = ratio_mat,
  beside = TRUE,                 # grouped bars
  col = age_colors,
  ylim = c(0, max(ratio_mat) + 5),
  ylab = "Mortality rate (%)",
  main = "Mortality rate by smoking status and age group",
  space = c(0.2, 1)
)

text(
  x = bp,
  y = ratio_mat,
  labels = paste0(ratio_mat, "%"),
  pos = 1,        # inside the bar
  cex = 1
)
legend(
  "topleft",
  legend = rownames(ratio_mat),
  fill = age_colors,
  title = "Age group",
  bty = "n"
)
```

<img width="801" height="468" alt="image" src="https://github.com/user-attachments/assets/69b02a55-45f4-4caf-909f-09ca9614ddbe" />

When the data are analyzed by age group, smokers show a higher mortality rate than non-smokers in each age category.

However, when all ages are combined, the overall result suggests the opposite. 

This change in the relationship after stratifying by age illustrates Simpson’s paradox, where a hidden variable (age) strongly influences the observed outcome.

## Question 3: - Logistic regression analysis
To avoid the bias introduced by arbitrary age groupings, a logistic regression model is used. 

Linear Regression is used when the target variable is continuous. As the response variable (Death) is binary (0 = Alive, 1 = Dead), linear regression is not appropiate .Because of that we use logistic regression that is used when the target variable is categorical.

TThe objective of the logistic regression is not only to visualize the data, but to model the relationship between the response variable (death) and an explanatory variable (age), in order to describe how mortality risk evolves continuously with age and to quantify the influence of age on this risk. Compared to aggregated analyses or discretized age groups, this approach reduces methodological bias and allows a clearer interpretation of the relationship between smoking and mortality by explicitly controlling for age as a confounding variable. Separate models are fitted for smokers and non-smokers, and the resulting curves show the estimated probability of death as a function of age, together with 95% confidence intervals.

### Implementation details:
We first define a binary outcome variable (Death = 1 if the individual died during the follow-up, 0 otherwise). Then, we fit two separate logistic regression models, one for smokers and one for non-smokers, in order to compare how the probability of death evolves with age in each group. Finally, we compute predicted probabilities and 95% confidence intervals over the observed age range to visualize the estimated risk profiles.

```{r}
data$Death <- ifelse(data$Status == "Dead", 1, 0)

model_nonsmokers <- glm(
  Death ~ Age,
  data = data[data$Smoker == "No", ],
  family = binomial
)

model_smokers <- glm(
  Death ~ Age,
  data = data[data$Smoker == "Yes", ],
  family = binomial
)

age_seq <- seq(min(data$Age, na.rm = TRUE), max(data$Age, na.rm = TRUE), by = 1)

pred_no <- predict(
  model_nonsmokers,
  newdata = data.frame(Age = age_seq),
  type = "link",
  se.fit = TRUE
)

pred_yes <- predict(
  model_smokers,
  newdata = data.frame(Age = age_seq),
  type = "link",
  se.fit = TRUE
)

# Convert from log-odds to probability
prob_no   <- plogis(pred_no$fit)
lower_no  <- plogis(pred_no$fit - 1.96 * pred_no$se.fit)
upper_no  <- plogis(pred_no$fit + 1.96 * pred_no$se.fit)

prob_yes  <- plogis(pred_yes$fit)
lower_yes <- plogis(pred_yes$fit - 1.96 * pred_yes$se.fit)
upper_yes <- plogis(pred_yes$fit + 1.96 * pred_yes$se.fit)

plot(
  age_seq, prob_no,
  type = "l",
  lwd = 2,
  col = "blue",
  ylim = c(0, 1),
  xlab = "Age",
  ylab = "Probability of death",
  main = "Logistic regression: Probability of Death as a function of Age (95% CI)"
)

# CI for non-smokers
lines(age_seq, lower_no, col = "blue", lty = 2)
lines(age_seq, upper_no, col = "blue", lty = 2)

# Smokers curve + CI
lines(age_seq, prob_yes, col = "red", lwd = 2)
lines(age_seq, lower_yes, col = "red", lty = 2)
lines(age_seq, upper_yes, col = "red", lty = 2)

legend(
  "topleft",
  legend = c("Non-smokers", "Smokers"),
  col = c("blue", "red"),
  lwd = 2,
  bty = "n"
)

```

<img width="827" height="518" alt="image" src="https://github.com/user-attachments/assets/bab56ede-e62c-4371-be1e-52fc9fccfd92" />

The graph shows that the probability of death increases with age for both smokers and non-smokers, reflecting the strong effect of age on mortality. For almost the entire age range, the curve corresponding to smokers lies above the curve for non-smokers, indicating a higher estimated mortality risk for smokers at the same age. This supports the interpretation that the paradox observed in the aggregated analysis is driven by confounding due to age. By modeling age as a continuous variable, the regression framework avoids arbitrary discretization and provides a clearer description of the association between smoking and mortality.
