# Proof by Contradiction

Proof by contradiction is a powerful technique used in mathematics to prove a statement by assuming the negation of what needs to be proven and deriving a contradiction. This method is based on the law of excluded middle, which states that a statement is either true or false.

## Definition

To prove a statement $P$, we assume its negation $\neg P$ is true and derive a logical contradiction. This contradiction arises when assuming both $P$ and $\neg P$ are true simultaneously, leading to the conclusion that the assumption that $\neg P$ is true must be false. Therefore, the original statement $P$ is true.

## Example

Let's consider the following statement for all integers $a$ and $b$: "If $a$ is even and $b$ is odd, then $a+b$ is odd." To prove this statement by contradiction, we assume the negation: "There exist integers $a$ and $b$ such that $a$ is even, $b$ is odd, and $a+b$ is not odd."

Assume $a$ is even, which means $a= 2k$ for some integer $k$, and $b$ is odd, which means $b= 2m+ 1$ for some integer $m$. Then $a+b= 2k+ 2m+ 1= 2(k+m)+ 1$. If $a+b$ is not odd, it must be even, so $a+b= 2n$ for some integer $n$. 

But this leads to a contradiction, as $2(k+m)+ 1$ cannot be of the form $2n$. Therefore, the assumption that $a+b$ is not odd is false, and the original statement holds true.

## Historical Context

Proof by contradiction has a long history dating back to ancient Greek mathematicians like Euclid, who used this method to prove the infinite nature of prime numbers in his *Elements*. It has since become a fundamental tool in mathematical reasoning, used in various branches of mathematics like analysis, number theory, and geometry.

## Real-life Example

Consider the statement: "There are infinitely many irrational numbers." To prove this statement by contradiction, we assume the negation: "There are finitely many irrational numbers." By considering known irrational numbers like $\sqrt{2}$ and $\pi$, we can construct a contradiction by showing the existence of infinitely many irrational numbers.

## Exam Questions

1. Prove by contradiction that $\sqrt{2}$ is irrational.
2. Use proof by contradiction to show that the sum of a rational number and an irrational number is irrational.
3. Show by contradiction that there are infinitely many prime numbers.