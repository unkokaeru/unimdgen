# Conditional Probability

Conditional probability is a fundamental concept in probability theory that quantifies the likelihood of an event occurring given that another event has already occurred. It is denoted by $P(A|B)$, which reads as "the probability of event $A$ given event $B$."

## Definition

The conditional probability of event $A$ given event $B$ is defined as:

$$
P(A|B)=\frac{P(A\cap B)}{P(B)},\text{ where} P(B)> 0$$

Here, $P(A\cap B)$ represents the probability of both event $A$ and event $B$ occurring.

## Interpretation

Conditional probability allows us to update the probability of an event based on additional information. For example, if there are two urns, one with 3 red balls and 2 blue balls, and the other with 2 red balls and 3 blue balls, and we randomly select an urn and then draw a red ball, the conditional probability of having selected the first urn given that we drew a red ball can be calculated using Bayes' theorem.

## Conditional Probability Formula

If $A$ and $B$ are two events, the formula for conditional probability can be rewritten as:

$$
P(A|B)=\frac{P(A\cap B)}{P(B)}=\frac{P(B|A)\cdot P(A)}{P(B)}$$

This form is known as the **multiplicative rule of probability**.

## Real-life Example

Consider a bag with 3 red balls and 2 green balls. You pick a ball at random, note its color, and then without replacing it, pick another ball. The event $A$ is selecting a green ball on the first draw, and event $B$ is selecting a red ball on the second draw. The probability of drawing a red ball on the second draw given that the first ball drawn was green is a classic example of conditional probability.

## History

The concept of conditional probability was first introduced by Thomas Bayes in the 18th century. Bayes' work laid the foundation for what would later be known as Bayes' theorem, a fundamental result in probability theory that provides a way to revise existing beliefs in the presence of new evidence.

## Exam Questions

1. Two fair six-sided dice are rolled. Given that the sum of the dice is 7, what is the probability that one of the dice shows a 4?
2. A box contains 3 red balls and 2 green balls. Two balls are drawn in succession without replacement. What is the probability that the second ball is green given that the first ball was red?
3. In a group of students, 60% are female and 40% are male. If 30% of the females and 50% of the males own a car, what is the probability that a randomly selected car owner is a female?

Remember, practice is key to mastering conditional probability!