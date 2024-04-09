# Basis Step

In mathematical induction, the **basis step** is the initial step of the induction where we prove the statement holds for the base case. The base case is typically the smallest value of the variable for which we need to prove the statement.

## Definition

Mathematical induction is a method of mathematical proof typically used to establish a given statement for all natural numbers. The basis step is the first part of the proof where we show that the statement holds for the smallest value(s) of the variable (often 0 or 1).

## Explanation

To start a proof by mathematical induction, we first prove that the statement is true for the base case. This provides the base for the induction to proceed to prove the statement for all other cases. The basis step establishes the foundation of the inductive proof.

For example, if we want to prove a statement P(n) is true for all natural numbers n, we first show that P(1) (or P(0)) is true. This forms the basis of our induction. If the statement is true for the base case, and we can prove that assuming it is true for some arbitrary k implies it is true for k + 1, then we can conclude that the statement is true for all natural numbers.

## Example

Let's consider the statement:

$$P(n)= 1+ 2+ 3+...+ n=\frac{n(n+1)}{2}$$

**Basis Step:** For n = 1, the LHS is 1 and the RHS is (1 * 2) / 2 = 1. Hence, the statement holds for n = 1.

## Historical Context

Mathematical induction was first introduced by Blaise Pascal in the 17th century. It has since become a fundamental technique in mathematics, particularly in combinatorics, number theory, and algebra. The idea of mathematical induction is rooted in the works of ancient Greek mathematicians such as Euclid.

## Real-life Example

Imagine you have a bunch of dominoes laid out in a row. To prove that pushing the first domino will cause all dominoes to fall, you start by pushing the first domino (basis step) and then show that if one domino falls, it will cause the next one to fall, thereby proving that all dominoes will fall.

## Exam Questions

1. Prove by mathematical induction that the sum of the first n odd numbers is $n^2$.
   
2. Using mathematical induction, prove that $2^n> n^2$ for all integers $n\geq 5$.
   
3. Show that the Fibonacci numbers are non-negative for all integers using mathematical induction.