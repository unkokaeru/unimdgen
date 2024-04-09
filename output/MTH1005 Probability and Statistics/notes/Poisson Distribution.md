# Poisson Distribution

The Poisson distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space. It is named after the French mathematician Siméon Denis Poisson.

## Definition

For a random variable $X$ that follows a Poisson distribution with parameter $\lambda> 0$, the probability mass function of $X$ is given by:

$$ P(X= k)=\frac{e^{-\lambda}\lambda^k}{k!},\quad\text{for} k= 0, 1, 2,\ldots$$

Here, $\lambda$ is the average rate of event occurrences in the interval. The mean and variance of a Poisson distribution are both equal to $\lambda$.

## Properties

1. The Poisson distribution is often used to model the number of events occurring in a fixed time interval, such as the number of emails received in an hour or the number of customers entering a store in a day.

2. It is a limiting case of the binomial distribution when the number of trials is large and the probability of success on each trial is small.

3. The Poisson distribution is memoryless, meaning that the probability of the next event occurring does not depend on the past. This property makes it useful for modeling random events where the occurrences are independent.

## Example

Suppose on average, 5 customers enter a store in an hour. What is the probability that exactly 3 customers will enter the store in the next hour, assuming the number of customers follows a Poisson distribution?

We can use the Poisson distribution formula to calculate:

$$ P(X= 3)=\frac{e^{-5} 5^3}{3!}\approx 0.1403$$

So, the probability of exactly 3 customers entering the store in the next hour is approximately 0.1403.

## Historical Context

The Poisson distribution was first introduced by Siméon Denis Poisson in the early 19th century while studying the frequency of deaths from mule kicks in the French army. He developed the distribution to model rare events that occurred at a constant rate, leading to its widespread use in various fields like insurance, telecommunications, and reliability engineering.

## Real-life Application

One real-life application of the Poisson distribution is in call centers to model the number of incoming calls during a certain period. By understanding the distribution of call arrivals, call centers can better allocate resources and optimize their operational efficiency.

## Exam Questions

1. Given a Poisson distribution with parameter $\lambda= 3$, calculate the probability of observing exactly 2 events.
2. Explain the concept of memorylessness in the context of the Poisson distribution.
3. A website receives an average of 100 visits per hour. Find the probability of having more than 120 visits in the next hour, assuming a Poisson distribution.