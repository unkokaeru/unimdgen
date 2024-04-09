# Probability Spaces

## Introduction
In probability theory, a **probability space** is a mathematical construct that represents the set of all possible outcomes of a random experiment along with the likelihood of each outcome occurring. It provides a formal framework for analyzing uncertain events and quantifying the probability of different outcomes.

## Definitions
1. **Sample Space (S):** The sample space is the set of all possible outcomes of a random experiment. Each outcome is represented by a point in the sample space.
   
2. **Event (E):** An event is a subset of the sample space, which represents a collection of possible outcomes that share a particular characteristic.

3. **Probability Function (P):** A probability function assigns a probability value to each event in the sample space. It satisfies the following properties:
    - For any event E, $ 0\leq P(E)\leq 1$ (probability lies between 0 and 1).
    - The probability of the entire sample space S is 1, i.e., $ P(S)= 1$.
    - For mutually exclusive events $ E_1, E_2,\ldots$, i.e., events that cannot occur simultaneously, the probability of their union is the sum of their individual probabilities: $ P(E_1\cup E_2\cup\ldots)= P(E_1)+ P(E_2)+\ldots$.

4. **Probability Space:** A probability space is defined as a triple $(S,\mathcal{F}, P)$, where:
    - $ S$ is the sample space,
    - $\mathcal{F}$ is a collection of events (a sigma-algebra) from $ S$,
    - $ P$ is the probability function that assigns probabilities to events in $\mathcal{F}$.

## Real-Life Example
Consider rolling a fair six-sided die. The sample space is $ S=\{1, 2, 3, 4, 5, 6\}$, where each outcome represents the number rolled on the die. An event could be "rolling an even number," represented by the subset $ E=\{2, 4, 6\}$. The probability of this event is $ P(E)=\frac{3}{6}=\frac{1}{2}$.

## Historical Context
The theory of probability spaces was pioneered by Andrey Kolmogorov in the 1930s. Kolmogorov's axioms provided a rigorous foundation for probability theory, leading to its widespread applications in various fields like statistics, finance, and physics.

## Exam Questions
1. Consider a biased coin with probability of landing heads being $\frac{2}{3}$. Define the sample space and a few events of interest for this experiment.
2. Prove that the probability of an event not occurring is $ 1- P(E)$, where $ E$ is any event in the sample space.
3. Explain the concept of independence of events in a probability space. Provide an example of two independent events and calculate the probability of their intersection.