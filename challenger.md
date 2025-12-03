Reproduction of the Challenge
---
Language: R  
Language version: 4.5.1 
Main libraries:
Tool:
Operating System: 

Coments about the project: 
---
a) 
-
After reviewing the dataset, we can see that not all measurements were taken under the same pressure conditions.
To ensure a consistent and valid comparison, I recommend removing all observations with Pressure ≠ 200, since temperature effects should be evaluated under the same pressure level. We also know that temperature depends on pressure, so mixing different pressure values would bias the analysis.

In addition, there is an invalid date ("7/2903/85") that should be removed.

b)
-
A new plot showing the ratio Malfunction/Count as a function of Temperature should be generated using the cleaned dataset.
[Temperture_filter_data.pdf](https://github.com/user-attachments/files/23916902/Temperture_filter_data.pdf)

c) 
-
The updated model fitted to the filtered data is:

Call:
glm(formula = Malfunction/Count ~ Temperature, family = binomial(link = "logit"), 
    data = data_filtered, weights = Count)

Coefficients:
            Estimate Std. Error z value Pr(>|z|)  
(Intercept)  3.96165    2.97440   1.332   0.1829  
Temperature -0.09372    0.04625  -2.026   0.0427 *
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 15.931  on 13  degrees of freedom
Residual deviance: 11.552  on 12  degrees of freedom
AIC: 27.289

Number of Fisher Scoring iterations: 5

When comparing these results with those reported in the original study, we can see that cleaning the data improves the model fit:
- The residual deviance improves from 18.086 (df = 21) to 11.552 (df = 12).
- The AIC improves from 35.647 to 27.289.

Therefore, we can say that the cleaned model provides a better fit than the model including observations that should be removed.

The new estimated parameters are:
- αˆ = 3.96165 and
- βˆ = -0.09372
- Standard error αˆ = 2.97440
- Standard error βˆ = 0.04625.
- The Residual deviance corresponds to the Goodness of fit G2 = 11.552 with 12 degrees of freedom.

d) Predicting failure probability
-
New plot: [Predicting failure probability_filter_data.pdf](https://github.com/user-attachments/files/23917376/Predicting.failure.probability_filter_data.pdf)

If we compare the new plot with the old plot, we can see that the updated model has a curve with a smaller slope. This means that the effect of temperature on the failure becomes weaker after cleaning the data. This change is expected because the original dataset included observations with different pressure levels. When we keep only the data with Pressure = 200, the model shows a more accurate and smoother effect of temperature.

e) Confidence on the prediction
-
