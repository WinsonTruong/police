# An Investigation of New York Police Department's Practice of Stop, Question, and Frisk

The protests of June 2020 demonstrate that all across America, the people were upset at the systemtic discrimination and violence that Black Americans have been experiencing for centuries. Of the countless injustices, now in mainstream focus thanks to the Black Lives Matter movement, this project will focus on the horrid racial profiling of Black people by the police.

#### This picture says it all
![Image 1](https://github.com/WinsonTruong/police/blob/master/images/frisk_v_arrest.png)


# Notion Page
This dedicated website explains the background knowledge and walks you through my methods. Highly recommended!
https://www.tinyurl.com/stopSQF/

# Questions 
1. What are the past behaviors and trends of officers who racially profile black people?
2. Are officers actually frisking an individual based on reasonable suspicion or just racially profiling?
3. Is SQF fair? Does SQF and policing at large have to be fair to begin with?

# Data
The primary data we will be using is [publicly available by the New York Police Department](https://www1.nyc.gov/site/nypd/stats/reports-analysis/stopfrisk.page). It contains every recording of stop, question, and frisk practices used in 2019. While data starting from 2003 is available, it does not follow the same layout year-by-year and often contains missing data. The cleaning process can be found in the 'notebooks' directory where there is a 'clean_and_impute.ipynb' notebook.

#### _A Glimpse at the Missing Data_

![Image 2](https://github.com/WinsonTruong/police/blob/master/images/missing_data.png)

In order to account for the missing values we will impute via [Multiple Imputation by Chained Equations](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3074241/)_.

Why Impute? Single imputation procedures such as replacing the data with the sample mean would mean I have to draw a decision boundary for my binary variables and with no prior knowledge, mean imputation could potentially accentuate bias. In order to maintain the relationship between the variables, I believe a Bayesian method that utilizes the other well-defined feature sets is best.

# EDA
Using the power of Tableau and Python, here are some visualizations of interest

Police behavior seems to change depending on when their shift is:
![Image 3](https://github.com/WinsonTruong/police/blob/master/images/bronx_queens.png)

Most of the time, it seems the low-level officers are conducting the stop and frisks

A Heatmap of Stops by Officer Rank
![Image 4](https://github.com/WinsonTruong/police/blob/master/images/police_rank.png)

A table describing the officers success rate 
![Image 5](https://github.com/WinsonTruong/police/blob/master/images/police_rank2.png)





# Results





* source: 
