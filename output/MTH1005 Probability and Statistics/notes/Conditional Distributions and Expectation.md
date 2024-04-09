# Conditional Distributions and Expectation

In probability theory, conditional distributions and conditional expectations are important concepts that help us model uncertainty when certain conditions are given. Let's dive into these concepts and explore their significance in various contexts.

## Conditional Distributions

### Definition
Let $(\Omega,\mathcal{F}, P)$ be a probability space and $X$ and $Y$ be two random variables defined on this space. The conditional distribution of $X$ given $Y=y$, denoted by $P(X\mid Y= y)$, is the probability distribution of $X$ when $Y$ is fixed at a particular value $y$.

### Properties
1. For a fixed $y$, $P(X\mid Y= y)$ is a valid probability distribution.
2. The conditional distribution $P(X\mid Y)$ is itself a random variable.

### Example
Consider rolling two fair six-sided dice $X$ and $Y$. Let $Z= X+ Y$ be the sum of the two dice. The conditional distribution of $Y$ given $Z=8$ can be determined by looking at all possible outcomes of the dice that sum up to 8. For each of these outcomes, the conditional probability will be $\frac{1}{36}$.

## Conditional Expectation

### Definition
Given random variables $X$ and $Y$, the conditional expectation of $X$ given $Y$, denoted by $E(X\mid Y)$, is the expected value of $X$ when $Y$ is fixed.

### Properties
1. The conditional expectation $E(X\mid Y)$ is a function of $Y$ and is a random variable. 
2. It satisfies the tower property: $E(E(X\mid Y))= E(X)$.

### Example
Suppose we have two random variables $X$ and $Y$ representing the number of heads obtained from flipping two different coins. The conditional expectation of $X$ given $Y=1$ would be equal to $E(X\mid Y=1)=\frac{1}{2}$.

## Applications
Conditional distributions and expectations find applications in various fields such as finance, machine learning, and statistics. In finance, they are used in modeling stock prices and predicting future values based on past information. In machine learning, they play a crucial role in building predictive models based on observed data.

## Historical Context
The concept of conditional probability was first introduced by Pierre-Simon Laplace in the 18th century as a way to update probabilities based on new information. Later, with the development of measure theory in the 20th century, the modern definition of conditional probability and expectation was formalized.

## Real-life Example
Consider a medical diagnosis scenario where a patient may exhibit symptoms $X$ and $Y$. The conditional distribution and expectation of the patient's illness given these symptoms can help doctors make informed decisions about the appropriate treatment.

---

### Practice Questions
1. Let $X$ and $Y$ be two independent random variables with means $\mu_X$ and $\mu_Y$, respectively. Calculate $E(XY\mid Y)$.
2. Given a fair six-sided die $X$ and a random variable $Y= X^2$, calculate $E(X\mid Y= 4)$.
3. Show that $E(E(X\mid Y))= E(X)$ using the tower property of conditional expectation.

Remember to fully understand the concepts of conditional distributions and expectations, as they form the basis for many advanced topics in probability theory and statistics.