# Binomial Distribution

The binomial distribution is a discrete probability distribution that describes the number of successes in a fixed number of independent Bernoulli trials, where each trial has the same probability of success, denoted by $p$.

## Definitions:

- **Bernoulli trial**: A random experiment with two possible outcomes, usually denoted as success (with probability $p$) and failure (with probability $1-p$).
- **Binomial distribution**: The probability distribution of the number of successes in a fixed number of Bernoulli trials, denoted by $n$.
- **Probability mass function (PMF)**: The function that gives the probability of each possible outcome of a discrete random variable.
- **Expectation**: The mean or average of a random variable, typically denoted by $\mu$.
- **Variance**: A measure of the spread of a distribution, usually denoted by $\sigma^2$.

## Formulas:

1. **Probability mass function**: 

The probability of getting exactly $k$ successes in $n$ trials is given by the formula:

$$P(X=k)=\binom{n}{k} p^k(1-p)^{n-k}$$

where $\binom{n}{k}$ is the binomial coefficient, which represents the number of ways to choose $k$ successes out of $n$ trials.

2. **Expectation and Variance**:

The expectation and variance of a binomial distribution are:

$$E(X)= np$$

$$Var(X)= np(1-p)$$

## Explanation:

Suppose we toss a fair six-sided die $10$ times and count the number of times the number $5$ appears. This scenario can be modeled using a binomial distribution, where each toss of the die is a Bernoulli trial with a probability of success (rolling a $5$) of $\frac{1}{6}$. The total number of successes (rolling a $5$) in $10$ independent trials follows a binomial distribution.

The binomial distribution is a fundamental concept in probability theory and has wide applications in various fields such as economics, genetics, and quality control. Understanding the binomial distribution helps us analyze random experiments and make predictions based on probabilities.

## Real-life Example:

Suppose a basketball player has a free-throw success rate of $70\%$. If she takes $100$ free-throw shots, we can model the number of successful shots using a binomial distribution with $n=100$ and $p=0.7$. We can calculate the probabilities of her making different numbers of shots out of $100$.

## Historical Context:

The binomial distribution is named after the Swiss mathematician Jacob Bernoulli, who introduced it in his work "Ars Conjectandi" in $1713$. It was later generalized and further studied by other prominent mathematicians such as Pierre-Simon Laplace and Carl Friedrich Gauss.

## Exam Questions:

1. A fair coin is tossed $8$ times. Find the probability of getting exactly $5$ heads.
2. A box contains $12$ red balls and $8$ blue balls. If $5$ balls are randomly drawn from the box without replacement, find the probability of getting exactly $3$ red balls.
3. In a multiple-choice test with $10$ questions, each question has $4$ choices. If a student guesses on each question, find the probability that the student gets at least $7$ questions correct.