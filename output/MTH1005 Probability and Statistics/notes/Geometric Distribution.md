# Geometric Distribution

In probability theory and statistics, the **geometric distribution** models the number of independent Bernoulli trials needed to get a success for the first time. Here, a **Bernoulli trial** is a random experiment with exactly two possible outcomes: success (with probability $p$) and failure (with probability $1-p$).

## Definition

Let $X$ be the number of trials needed to obtain the first success in a sequence of independent Bernoulli trials, each with probability of success $p$. The probability mass function of the geometric distribution is given by:

$$
P(X= k)=(1-p)^{k-1} p\quad\text{for} k= 1, 2, 3,\ldots$$

## Properties

1. The mean (expected value) of a geometric distribution is $\frac{1}{p}$.
2. The variance of a geometric distribution is $\frac{1-p}{p^2}$.
3. The geometric distribution is memoryless, meaning that if $X$ is the number of trials until the first success and $Y$ is the number of additional trials needed after $X$ trials, then the conditional distribution of $Y$ given $X> k$ is the same as the unconditional distribution of $Y$, for all $k$.

## Example

Suppose you are flipping a fair coin (probability of heads $0.5$) until you get heads for the first time. Let $X$ be the random variable representing the number of flips needed. The probability of getting heads on the first flip is $0.5$, getting heads on the second flip (after one tail) is $(1-0.5)\times 0.5= 0.25$, and so on. The probability mass function can be calculated using the formula above.

## Historical Context

The geometric distribution has a rich history in probability theory and statistics, dating back to the 18th century when Swiss mathematician Daniel Bernoulli introduced the concept of Bernoulli trials. The geometric distribution was later formalized and studied extensively by French mathematician Emile Borel in the early 20th century.

## Real-life Applications

The geometric distribution finds applications in various real-life scenarios such as:

- Modeling the number of trials needed to achieve the first success in gambling games.
- Estimating the number of phone calls a call center operator must make to get the first sale.
- Analyzing the number of attempts needed to solve a puzzle.

## Exam Questions

1. Suppose a biased coin has a probability of coming up heads as $0.3$. What is the probability that the first head appears on the 4th flip?
2. Calculate the mean and variance of a geometric distribution with probability of success $0.2$.
3. Explain the concept of memorylessness in the context of the geometric distribution.