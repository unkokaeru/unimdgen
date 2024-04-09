# Proof Techniques

## Introduction
In mathematics, proofs are fundamental to verifying the correctness of mathematical statements. There are various proof techniques used to demonstrate the truth of a statement or theorem. Understanding these proof techniques is essential for any mathematician to excel in the field of mathematics.

## Direct Proof
A direct proof is a fundamental proof technique where we start with the given premises and use logical deductions to arrive at the conclusion. In a direct proof, we assume that the premise is true and show that, under this assumption, the conclusion must also be true.

**Example:** Prove that for all integers *a* and *b*, if *a* is even and *b* is even, then *a+b* is even.

*Proof:* Let *a* and *b* be even integers. By definition, there exist integers *m* and *n* such that *a = 2m* and *b = 2n*. Adding *a* and *b*, we get *a + b = 2m + 2n = 2(m + n)*, which is an even number. Therefore, the sum of two even integers is even.

## Proof by Contradiction
Proof by contradiction is a powerful proof technique where we assume the negation of what we want to prove and show that this leads to a contradiction. If assuming the opposite of what we want to prove results in a logical inconsistency, then our original statement must be true.

**Example:** Prove that the square root of 2 is irrational.

*Proof:* Suppose by contradiction that $\sqrt{2}$ is rational. Then, there exist integers *a* and *b* such that $\sqrt{2}=\frac{a}{b}$, where *a* and *b* have no common factors. Squaring both sides gives $2=\frac{a^2}{b^2}$. This implies $a^2= 2b^2$. Since the right-hand side is even, the left-hand side must also be even. This means *a* must be even. If *a* is even, then $a^2$ is divisible by 4. Thus, $2b^2$ is divisible by 4, implying *b* is also even. But this contradicts our assumption that *a* and *b* have no common factors. Hence, $\sqrt{2}$ is irrational.

## Proof by Mathematical Induction
Proof by mathematical induction is a technique used to prove statements about natural numbers. The method consists of two steps: the base case and the inductive step. In the base case, we prove that the statement holds for the smallest value. In the inductive step, we assume that the statement holds for some arbitrary *k* and then show that this implies the statement holds for *k+1*.

**Example:** Prove that $1+ 2+ 3+\ldots+ n=\frac{n(n+1)}{2}$ for all positive integers *n*.

*Base Case:* For *n = 1*, $1=\frac{1(1+1)}{2}$ is true.

*Inductive Step:* Assume the statement is true for *k*, i.e., $1+ 2+ 3+\ldots+ k=\frac{k(k+1)}{2}$. Then we need to show that $1+ 2+ 3+\ldots+ k+(k+1)=\frac{(k+1)(k+2)}{2}$. Adding *k+1* to both sides of the assumed equation gives $\frac{k(k+1)}{2}+(k+1)=\frac{(k+1)(k+2)}{2}$. After simplifying, this equation is true. Hence, by mathematical induction, the statement is true for all positive integers *n*.

## Three Exam Questions:
1. Prove using a direct proof that the sum of two odd integers is even.
2. Prove by contradiction that there are infinitely many prime numbers.
3. Prove using mathematical induction that $1^2+ 2^2+\ldots+ n^2=\frac{n(n+1)(2n+1)}{6}$ for all positive integers *n*.