# Union and Intersection

In set theory, the union and intersection of sets are fundamental operations that allow us to combine or compare different sets based on certain conditions. Let's consider two sets, denoted by $A$ and $B$.

## Union of Sets

The *union* of two sets $A$ and $B$, denoted by $A\cup B$, is the set of all elements that are in $A$, in $B$, or in both $A$ and $B$. Symbolically,

$$ A\cup B=\{x\mid x\in A\text{ or} x\in B\}.$$

For example, if $A=\{1, 2, 3\}$ and $B=\{3, 4, 5\}$, then the union $A\cup B$ is $\{1, 2, 3, 4, 5\}$.

## Intersection of Sets

The *intersection* of two sets $A$ and $B$, denoted by $A\cap B$, is the set of all elements that are both in $A$ and in $B$. Symbolically,

$$ A\cap B=\{x\mid x\in A\text{ and} x\in B\}.$$

For example, if $A=\{1, 2, 3\}$ and $B=\{3, 4, 5\}$, then the intersection $A\cap B$ is $\{3\}$.

## Properties

### Commutative Laws:

1. $A\cup B= B\cup A$
2. $A\cap B= B\cap A$

### Associative Laws:

1. $(A\cup B)\cup C= A\cup(B\cup C)$
2. $(A\cap B)\cap C= A\cap(B\cap C)$

### Distributive Laws:

1. $A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$
2. $A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$

### De Morgan's Laws:

1. $(A\cup B)'= A'\cap B'$
2. $(A\cap B)'= A'\cup B'$

## Real-life Example

Consider two sets: $A$ is the set of students who study mathematics, and $B$ is the set of students who study physics. The union $A\cup B$ represents all students who study either mathematics or physics or both. The intersection $A\cap B$ represents students who study both mathematics and physics.

## Historical Context

The concepts of union and intersection in set theory were introduced by Georg Cantor in the late 19th century as part of his development of a rigorous foundation for mathematics. Cantor's work on set theory laid the groundwork for modern mathematical analysis and led to the study of infinite sets.

## Exam Questions

1. Given $A=\{1, 2, 3\}$ and $B=\{2, 3, 4\}$, find $A\cap B$ and $A\cup B$.
2. Prove that the union of two sets is associative, i.e., show that $(A\cup B)\cup C= A\cup(B\cup C)$ for any sets $A$, $B$, and $C$.
3. If $A$ and $B$ are sets, show that $A\cap B\subseteq A$.