# Covariance and Correlation

In statistics, **covariance** and **correlation** are measures of the relationship between two random variables. They provide insights into how the variables change together.

## Covariance

The **covariance** between two random variables $X$ and $Y$, denoted as $\text{Cov}(X, Y)$, measures how much two variables change together. If the covariance is positive, it means that as one variable increases, the other variable tends to also increase. If the covariance is negative, it means that as one variable increases, the other variable tends to decrease. Covariance is calculated as:

$$\text{Cov}(X, Y)=\frac{1}{n}\sum_{i=1}^{n}(X_i-\bar{X})(Y_i-\bar{Y})$$

where $n$ is the number of data points, $X_i$ and $Y_i$ are individual data points, $\bar{X}$ and $\bar{Y}$ are the means of $X$ and $Y$ respectively.

However, interpreting covariance alone can be challenging because it is not standardized and depends on the scales of the variables.

## Correlation

**Correlation** overcomes the scale dependency of covariance by standardizing the measure. The **correlation coefficient** between two random variables $X$ and $Y$, denoted as $\rho(X, Y)$ or $r_{XY}$, is given by:

$$\rho(X, Y)=\frac{\text{Cov}(X,Y)}{\sigma_X\cdot\sigma_Y}$$

where $\sigma_X$ and $\sigma_Y$ are the standard deviations of $X$ and $Y$ respectively. The correlation coefficient ranges between -1 and 1. A correlation of 1 indicates a perfect positive relationship, -1 indicates a perfect negative relationship, and 0 indicates no relationship between the variables.

## Real-life Example

Imagine you have data on the amount of time spent studying for an exam (measured in hours) and the score achieved in the exam (out of 100). By calculating the correlation between these two variables, you can determine if there is a significant relationship between study time and exam score.

## Historical Context

Covariance was introduced by the famous statistician Francis Galton in the late 19th century. He used it to study the relationship between the heights of parents and their children. Later, Karl Pearson developed the concept of correlation as a standardized version of covariance.

## Exam Questions

1. Calculate the covariance between two random variables $X$ and $Y$ with the following data points: $(X_1, Y_1)=(2, 5)$, $(X_2, Y_2)=(3, 4)$, $(X_3, Y_3)=(5, 6)$.
   
2. If the correlation coefficient between two variables $X$ and $Y$ is 0.8, what does this indicate about their relationship?

3. Discuss the limitations of using covariance as a measure of relationship between variables and how correlation overcomes these limitations.