# An Investigation of New York Police Department's Practice of Stop, Question, and Frisk

The protests of June 2020 demonstrate that all across America, the people were upset at the systemtic discrimination and violence that Black Americans have been experiencing for centuries. Of the countless injustices, now in mainstream focus thanks to the Black Lives Matter movement, this project will focus on the horrid racial profiling of Black people by the police.

#### This picture says it all:
![Image 1a](https://github.com/WinsonTruong/police/blob/master/images/frisk_v_arrest2.png)


# Notion Page
[This dedicated website](https://www.tinyurl.com/stopSQF/) explains the background knowledge and walks you through all the my modeling decisions. 


# Questions 
1. What are the past behaviors and trends of officers who racially profile black people?
2. Are officers actually frisking an individual based on reasonable suspicion or just racially profiling?
3. Is SQF fair? Does SQF and policing at large have to be fair to begin with?

# Data
The primary data we will be using is [publicly available by the New York Police Department](https://www1.nyc.gov/site/nypd/stats/reports-analysis/stopfrisk.page). It contains every recording of stop, question, and frisk practices used in 2019. While data starting from 2003 is available, it does not follow the same layout year-by-year and often contains missing data. The cleaning process can be found in the 'notebooks' directory where there is a 'clean_and_impute.ipynb' notebook.

#### _A Glimpse at the Missing Data_

![Image 2](https://github.com/WinsonTruong/police/blob/master/images/missing_data.png)

In order to account for the missing values we will impute via [Multiple Imputation by Chained Equations](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3074241/).

Why Impute? Single imputation procedures such as replacing the data with the sample mean would mean I have to draw a decision boundary for my binary variables and with no prior knowledge, mean imputation could potentially accentuate bias. In order to maintain the relationship between the variables, I believe a Bayesian method that utilizes the other well-defined feature sets is best.

# EDA
Using the power of Tableau and Python, here are some visualizations of interest

Police behavior seems to change depending on when their shift is:
![Image 3](https://github.com/WinsonTruong/police/blob/master/images/bronx_queens.png)

The heatmap below shows that most stop and frisks are done by daytime patrol officers
![Image 4](https://github.com/WinsonTruong/police/blob/master/images/police_rank.png)

And overall, they seem to be stopping on false assumptions as indicated by their low success rate.
![Image 5](https://github.com/WinsonTruong/police/blob/master/images/police_rank2.png)


# Models and Feature Selection

I will use 3 different feature sets, with increasing complexity, for each of the 4 models. 


**Feature Sets**      | **Models**
--------------------- | -------------
Race                  | Logistic Regression (Baseline)
Appearance            | Logistic Regression + LASSO
Context               | SVM with Linear Kernel
\                     | SVM with Gaussian Kernel

**Comparison Statistics** | **Outputs**
------------------------  | -------------
F1 Score                  | Comparison Table
False Discovery Rate      | ROC Curves

#### _Why the LASSO?_
I could penalize/erase potentially insignificant features like hair color which could lead to more generalizability

#### _Why SVM with Differeing Kernels?_
- the data might not be linearly seperable, in which the SVM can handle the high dimensionality
- there is a decently large sample size
- I want to understand the tradeoff between speed/burn-in time relative to accuracy

#### _Why the F1 Score?_
I'm interested in how sure officers are that the suspect has contraband/weaspons (precision), but also how many suspects they are frisking at large (recall) because I'm interested in the racial profiling of Black people. Taking the harmonic mean of these two metrics seems quite fitting.

#### _Why the False Discovery Rate?_
I'm also interested in when my model is incorrect because an error in the context of policing could lead to claims of racial profiling by the police. While FDR-control is not the point of this project it is a very interesting idea.



# Results

![Image 6](https://github.com/WinsonTruong/police/blob/master/images/summary_metrics.png)

**Some Observations**
1. The F1 Score seems to hover around (0.5, 0.58). While this isn't the highest ideal score, we can see that adding 'Appearance' helps by about 0.05 and 'Context' features by about 0.01. While my model doesn't account for all latent variables, **officers are classifying primarily based on race.**
2. In terms of the F1 Score, the Logistic LASSO outperforms the other 3 models in the 'Race' and 'Context' feature sets.
3. Given all our models and datasets, the FDR approximately ranges from (0.36,  0.43). That means our models predicts that officers are frisking individuals on **un**-reasonable suspicion about 40% of the time. Read more about the [future studies here](https://www.notion.so/winsontruong/Conclusion-ae24f3b9aa0b4b678eadc2375c39c578)!


