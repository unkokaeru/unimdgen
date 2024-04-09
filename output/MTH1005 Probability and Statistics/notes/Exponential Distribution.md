# Exponential Distribution

The exponential distribution is a continuous probability distribution that describes the time between events in a Poisson point process, where events occur continuously and independently at a constant average rate. This distribution is widely used in various fields, including reliability engineering, queuing theory, and survival analysis.

## Probability Density Function (PDF)

The probability density function of the exponential distribution is given by:

$$
f(x;\lambda)=\begin{cases}\lambda e^{-\lambda x}&\text{for} x\geq 0,\\ 0&\text{for} x< 0,\end{cases}$$

where $\lambda> 0$ is the rate parameter. The mean and variance of the exponential distribution are both equal to $1/\lambda$.

## Cumulative Distribution Function (CDF)

The cumulative distribution function of the exponential distribution is given by:

$$
F(x;\lambda)=\begin{cases} 1- e^{-\lambda x}&\text{for} x\geq 0,\\ 0&\text{for} x< 0.\end{cases}$$

## Properties

- **Memorylessness**: One key property of the exponential distribution is that it is memoryless. This means that the probability of an event occurring after a certain time $t$ given that it has not occurred before $t$ is the same as the probability of the event occurring after time $t$, i.e., $P(X> s+t| X> s)= P(X> t)$.

- **Connection to Poisson Distribution**: If $X$ follows an exponential distribution with rate parameter $\lambda$, then the number of events in a unit time interval follows a Poisson distribution with parameter $\lambda$.

## Applications

- **Survival Analysis**: In medical research, the exponential distribution is used to model the time until the occurrence of an event of interest, such as the failure of a treatment or the occurrence of a disease.

- **Queuing Theory**: The exponential distribution is commonly used to model the interarrival times of customers in a queuing system.

- **Reliability Engineering**: It is used to model the time until failure of a system or component.

## Example

Suppose the time between two customers arriving at a store follows an exponential distribution with a rate parameter of $\lambda= 0.2$ customers per minute. Calculate the probability that the next customer will arrive within 5 minutes.

**Solution:**

The probability can be computed using the cumulative distribution function:

$$\begin{aligned}
P(X\leq 5)&= 1- e^{-0.2\times 5}\\&= 1- e^{-1}\\&\approx 0.6321.\end{aligned}$$

So, there is approximately a 63.21% chance that the next customer will arrive within 5 minutes.

## Historical Context

The exponential distribution was first introduced by the French mathematician Simon-Denis Poisson in the early 19th century in his study of the number of discrete events that occur in a fixed interval of time. It was later named the exponential distribution by the Swedish mathematician Andrey Markov in the late 19th century due to its connection with exponential functions.

## Exam Questions

1. Define the exponential distribution and explain its key properties.
2. Given an exponential distribution with a rate parameter of $\lambda= 0.3$, calculate the mean and variance of the distribution.
3. In a queuing system, the time between two arrivals of customers follows an exponential distribution with a rate parameter of $\lambda= 0.1$ per minute. Calculate the probability that the next customer will arrive within 10 minutes.