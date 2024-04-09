# Markov Chains

## Introduction
Markov chains are stochastic processes that involve a sequence of random variables, where the future state of the system depends only on the current state and not on the sequence of events that preceded it. They are named after the Russian mathematician Andrey Markov, who first introduced the concept in the early 20th century.

## Definitions
1. **State Space**: The set of all possible states that the system can be in.
2. **Transition Probability**: The probability of moving from one state to another in one step.
3. **Transition Matrix**: A matrix whose (i, j)-entry represents the probability of transitioning from state i to state j.
4. **Homogeneity**: The transition probabilities do not change over time. This property is known as time-homogeneous Markov chains.
5. **Chapman-Kolmogorov Equation**: It describes the evolution of the chain over multiple time steps. For a two-step transition, it states that the probability of going from state i to state j in two steps is the sum over k of the probability of going from state i to state k in one step times the probability of going from state k to state j in one step.

## Example
Consider a weather model with three states: sunny, cloudy, and rainy. The transition matrix might look like:

$$
P=\begin{bmatrix}
0.7& 0.2& 0.1\\
0.3& 0.4& 0.3\\
0.2& 0.3& 0.5\end{bmatrix}$$

This matrix shows the probabilities of transitioning from one weather state to another in a single day.

## Applications
Markov chains are used in various fields such as:
- **Finance**: Modeling stock prices.
- **Biology**: Modeling genetic drift.
- **Computer Science**: PageRank algorithm by Google.

## Historical Context
Andrey Markov first introduced Markov chains while studying the sequences of vowels in Eugene Onegin, a novel by Alexander Pushkin. His work laid the foundation for the study of stochastic processes.

## Exam Questions
1. Define a Markov chain and explain the concept of state space.
2. What does it mean for a Markov chain to be time-homogeneous?
3. Given a transition matrix, how would you calculate the probability of moving from one state to another in two steps?

Remember, practice makes perfect in understanding Markov chains!