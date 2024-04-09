# Expectation and Variance

In probability theory, the **expectation** of a random variable is a measure of its central tendency. It represents the average value that the random variable would take over an infinite number of repetitions of the random experiment. The expectation of a random variable $X$ is denoted by $\mathbb{E}[X]$, or sometimes simply as $\mu$.

For a discrete random variable $X$ with probability mass function $p(x)$, the expectation is given by:

$$\mathbb{E}[X]=\sum_{x} x\cdot p(x)$$

For a continuous random variable $X$ with probability density function $f(x)$, the expectation is given by:

$$\mathbb{E}[X]=\int_{-\infty}^{\infty} x\cdot f(x) dx$$

The **variance** of a random variable is a measure of how much the values of the random variable differ from the expectation. It gives a sense of the spread of the values around the mean. The variance of a random variable $X$ is denoted by $\text{Var}(X)$.

For a random variable $X$, the variance is calculated as:

$$\text{Var}(X)=\mathbb{E}[(X-\mu)^2]=\mathbb{E}[X^2]-(\mathbb{E}[X])^2$$

where $\mu=\mathbb{E}[X]$.

One important property of the variance is that it is always non-negative: $\text{Var}(X)\geq 0$.

### Example:

Consider a fair six-sided die. Let $X$ be the random variable representing the outcome of a single roll of the die. The probability mass function of $X$ is given by:

$$p(x)=\frac{1}{6}\quad\text{ for} x\in\{1, 2, 3, 4, 5, 6\}$$

Then, the expectation of $X$ is:

$$\mathbb{E}[X]=\sum_{x=1}^{6} x\cdot p(x)=\frac{1}{6}\cdot(1+ 2+ 3+ 4+ 5+ 6)= 3.5$$

The variance of $X$ can be calculated as:

$$\text{Var}(X)=\mathbb{E}[X^2]-(\mathbb{E}[X])^2=\sum_{x=1}^{6} x^2\cdot p(x)- 3.5^2=\frac{91}{6}-\frac{49}{4}=\frac{35}{12}$$

### Historical Context:

The concept of expectation was introduced by the French mathematician and physicist Abraham de Moivre in the early 18th century. Later, the concept of variance was developed by the English mathematician Ronald Fisher in the early 20th century. These concepts play a fundamental role in probability theory and statistics.

### Real-Life Example:

Suppose you are playing a game in which you can win $10$ dollars with probability $0.6$, or lose $5$ dollars with probability $0.4$. Let $X$ be the random variable representing your winnings. The expectation of $X$ tells you the average amount you expect to win (or lose) per game, while the variance gives you an idea of the variability in your winnings.

### Exam Questions:

1. Calculate the expectation of a fair coin flip, where $X$ is the random variable representing the outcome (Heads or Tails).
2. Let $Y$ be a continuous random variable with PDF $f(y)= 2y$ for $0\leq y\leq 1$. Calculate the variance of $Y$.
3. Suppose you have a biased die with probabilities $p(1)= 0.2$, $p(2)= 0.3$, $p(3)= 0.1$, $p(4)= 0.2$, $p(5)= 0.1$, $p(6)= 0.1$. Calculate the expectation and variance of the random variable representing the outcome of a single roll.