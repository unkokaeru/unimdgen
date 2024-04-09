# Confidence Intervals

In statistics, a **confidence interval** is a range of values that is likely to contain an unknown population parameter, the estimated range being calculated from a given set of sample data. The parameter is an unknown constant that represents a characteristic of a population, such as the mean or standard deviation.

## Understanding Confidence Intervals

1. **Level of Confidence**: This represents the probability that the interval will contain the true population parameter. Common levels of confidence include 90%, 95%, and 99%. For example, a 95% confidence level means that if we were to take 100 different samples and construct a confidence interval for each sample, we would expect approximately 95 of the intervals to contain the true population parameter.

2. **Margin of Error**: This is the amount added to and subtracted from the sample mean in order to construct the interval. It is also influenced by the level of confidence. Higher confidence levels will result in wider confidence intervals, and therefore larger margin of error.

3. **Formula**: The formula for a confidence interval for the population mean, assuming a normally distributed sample, is given by:

$$\bar{x}\pm z\left(\frac{s}{\sqrt{n}}\right)$$

where:
- $\bar{x}$ is the sample mean,
- $ s$ is the sample standard deviation,
- $ n$ is the sample size,
- $ z$ is the z-score corresponding to the desired confidence level, usually found using a standard normal distribution table.

## Example

Suppose we want to estimate the average height of students in a university. A random sample of 50 students is taken, and their average height is found to be 170 cm with a standard deviation of 10 cm. If we want to construct a 95% confidence interval for the population mean height, and the z-score for 95% confidence is 1.96, the confidence interval would be:

$$ 170\pm 1.96\left(\frac{10}{\sqrt{50}}\right)$$

## Historical Context

Confidence intervals were introduced by Jerzy Neyman in the 1930s as part of the development of modern statistical theory. The concept of using intervals instead of point estimates provides more information about the uncertainty of our estimates based on sample data.

## Real-life Application

In medical research, confidence intervals are commonly used to provide a range within which we are reasonably confident that the true effect size of a treatment lies. This information is crucial in decision-making processes regarding the effectiveness of different medical interventions.

## Exam Questions

1. Given a sample of 100 observations with a mean of 25 and standard deviation of 5, calculate a 90% confidence interval for the population mean.
   
2. Explain why increasing the level of confidence in a confidence interval leads to a wider interval.
   
3. Discuss the importance of confidence intervals in hypothesis testing and statistical inference.