# Limit of a Sequence

In real analysis, the concept of the limit of a sequence plays a central role. Understanding the limit of a sequence is crucial in many areas of mathematics, as it provides a precise way to describe the behavior of the terms in a sequence as the sequence progresses to infinity. 

## Definition

Let $(a_n)$ be a sequence of real numbers. We say that a real number $L$ is the **limit** of the sequence $(a_n)$ if, for every $\epsilon> 0$, there exists a natural number $N$ such that for all $n\geq N$, $|a_n- L|<\epsilon$.

This can be written symbolically as

$$\lim_{n\to\infty} a_n= L.$$

Here, $n$ is the index of the terms in the sequence, and $L$ is the limit that the terms approach as $n$ tends to infinity.

## Intuition

Intuitively, the limit of a sequence can be thought of as the value that the terms of the sequence converge to as $n$ becomes very large. This concept is closely related to the idea of convergence in mathematics, where a sequence converges if its terms eventually get arbitrarily close to a single value as $n$ increases.

## Examples

1. **Example 1**: Consider the sequence $(a_n)=\left(\dfrac{1}{n}\right)$. As $n$ approaches infinity, the terms of the sequence get arbitrarily close to $0$. Therefore, $\lim_{n\to\infty}\dfrac{1}{n}= 0$.

2. **Example 2**: Let $(b_n)=\left(\dfrac{1}{2^n}\right)$. As $n$ grows, the terms of the sequence become smaller and approach $0$. Thus, $\lim_{n\to\infty}\dfrac{1}{2^n}= 0$.

## Historical Context

The concept of the limit of a sequence has its roots in the development of calculus by mathematicians like Isaac Newton and Gottfried Wilhelm Leibniz in the 17th century. The foundational ideas of limits laid the groundwork for the rigorous study of calculus and analysis, allowing mathematicians to work with infinitely small and infinitely large quantities in a precise and well-defined manner.

## Real-life Applications

The notion of the limit of a sequence is not just a theoretical concept; it finds applications in various real-world scenarios. For example, in finance, the concept of a limit is used in modelling stock prices and predicting future trends based on historical data. Additionally, in computer science, limits are essential in analysing algorithms and optimizing their performance.

## Exam Questions

1. Determine the limit of the sequence $(c_n)=\left(\dfrac{n^2+ 3n}{2n^2+ n}\right)$ as $n$ tends to infinity.
   
2. Prove that the sequence $(d_n)=\left(\dfrac{n^2}{n^2+ 1}\right)$ converges and find its limit.
   
3. Consider the sequence $(e_n)=\left(\dfrac{(-1)^n}{n}\right)$. Does this sequence converge? Justify your answer.

By mastering the concept of the limit of a sequence, mathematicians gain a powerful tool for understanding the behavior of mathematical objects as they evolve over time or approach infinity.