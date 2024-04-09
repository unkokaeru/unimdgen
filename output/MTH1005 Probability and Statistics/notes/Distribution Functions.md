# Distribution Functions

In probability theory and statistics, a **distribution function** (also known as a **cumulative distribution function** or **CDF**) is a function that maps a value to its probability of occurrence. 

## Definition

For a random variable $X$, the distribution function $F(x)$ is defined as:

$$F(x)= P(X\leq x)$$

Where:
- $F(x)$ is the probability that the random variable $X$ takes on a value less than or equal to $x$.
- $P(X\leq x)$ is the probability that the random variable $X$ is less than or equal to $x$.

## Properties

1. $0\leq F(x)\leq 1$ for all $x$.
2. $F(x)$ is non-decreasing, meaning if $x_1< x_2$, then $F(x_1)\leq F(x_2)$.

## Types of Distribution Functions

1. **Discrete Distribution Function**: Used for discrete random variables.
2. **Continuous Distribution Function**: Used for continuous random variables.

### Example

Let's consider the discrete random variable $X$ representing the number shown on a fair six-sided die. The distribution function $F(x)$ for this random variable would be:

$$
F(x)=\begin{cases}
0,&\text{for} x< 1\\
1/6,&\text{for} 1\leq x< 2\\
1/3,&\text{for} 2\leq x< 3\\
1/2,&\text{for} 3\leq x< 4\\
2/3,&\text{for} 4\leq x< 5\\
5/6,&\text{for} 5\leq x< 6\\
1,&\text{for} x\geq 6\\\end{cases}$$

## Historical Context

The concept of distribution functions dates back to the work of mathematicians like Bernoulli and Laplace in the 18th century. Laplace made significant contributions to the theory of probability and used distribution functions to study the behaviour of random variables.

## Real-life Examples

- **Weather Forecast**: In meteorology, distribution functions can be used to model the probability of certain weather conditions occurring.
- **Stock Market Analysis**: Financial analysts use distribution functions to calculate the probability of different stock price movements.

## Exam Questions

1. Define a distribution function and explain its properties.
2. Consider a continuous random variable $Y$ with the following distribution function: $F(y)= 1- e^{-2y}$ for $y\geq 0$. Calculate $P(Y> 1)$.
3. A random variable $Z$ has a discrete distribution function given by: $F(z)= 0$ for $z< 1$, $F(z)= 1/3$ for $1\leq z< 2$, and $F(z)= 1$ for $z\geq 2$. Find the probability $P(1< Z\leq 2)$.

Remember, practice and application are key to mastering distribution functions.