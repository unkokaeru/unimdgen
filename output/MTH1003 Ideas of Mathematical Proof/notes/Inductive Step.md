# Inductive Step

In mathematics, the inductive step is a crucial component of proofs by mathematical induction. Mathematical induction is a powerful technique used to prove statements about natural numbers. The inductive step is the step where we show that if a statement is true for a particular natural number, then it is also true for the next natural number.

## Definition

Let's consider a statement P(n) that depends on a natural number n. To prove that P(n) is true for all natural numbers, we use mathematical induction, which consists of two steps:

1. **Base Case:** We first prove that P(1) is true.
2. **Inductive Step:** We assume that P(k) is true for an arbitrary natural number k ≥ 1. Then, we prove that this assumption implies P(k + 1) is true.

The inductive step is what allows us to extend the truth of a statement from one natural number to the next and therefore, to all natural numbers.

## Explanation

The inductive step is often essential in proving properties of sequences, series, divisibility rules, inequalities, and more. It is based on the principle that if we can show that a statement is true for one particular number and if the truth of the statement for that number implies the truth of the statement for the next number, then the statement is true for all natural numbers.

The inductive step is a form of deductive reasoning where we establish a logical link between the truth of a statement for a specific natural number and the truth for the next natural number.

## Example

Let's prove the formula for the sum of the first n natural numbers using mathematical induction. The formula states that for all natural numbers n:

$$1+ 2+ 3+\ldots+ n=\frac{n(n+1)}{2}$$

### Base Case:
For n = 1, the left-hand side is 1 and the right-hand side is (1*(1+1))/2 = 1. So, the base case holds.

### Inductive Step:
Assume the formula holds for some k ≥ 1, that is:

$$1+ 2+ 3+\ldots+ k=\frac{k(k+1)}{2}$$

Now, we need to prove that if the formula holds for k, then it also holds for k **k+1**. 

Adding **(k+1)** to both sides of the assumed formula, we get:

$$1+ 2+ 3+\ldots+ k+(k+1)=\frac{k(k+1)}{2}+(k+1)$$
$$\frac{k(k+1)}{2}+(k+1)=\frac{(k+1)(k+2)}{2}$$

Therefore, the formula holds for k+1 as well.

By the principle of mathematical induction, the formula is proven to be true for all natural numbers.

## Historical Context

Mathematical induction was first discovered and used by **Blaise Pascal** in the 17th century. It was later popularized by **Carl Friedrich Gauss** and **Augustus de Morgan**. The technique has since become a fundamental tool in mathematics, used to prove countless theorems and properties.

## Real-Life Example

Imagine you have a row of dominoes, each placed at an equal distance from one another. You want to prove that if you push the first domino and it falls, then all the dominoes in the row will fall. This is similar to the inductive step in mathematical proofs. You show that if one domino falls (base case), then the next one will fall, and so on, proving that all dominoes will fall eventually.

---

### Exam Questions:

1. Prove by induction that the sum of the first n odd numbers is $n^2$.
  
2. Use mathematical induction to show that $2^n> n^2$ for all integers n ≥ 5.
  
3. Consider the Fibonacci sequence where $F(0)= 0, F(1)= 1,$ and $F(n)= F(n-1)+ F(n-2)$ for $n\geq 2$. Prove by induction that $F(n)< 2^n$ for all non-negative integers n.

Remember, the inductive step is a powerful tool in your mathematical arsenal to prove statements about natural numbers and beyond!