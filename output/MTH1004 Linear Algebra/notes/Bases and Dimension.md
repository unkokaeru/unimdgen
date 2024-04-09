# Bases and Dimension

In linear algebra, a **basis** for a vector space $V$ over a field $F$ is a set of vectors that are linearly independent and that span $V$. That is, any vector in $V$ can be written as a unique linear combination of the basis vectors. The number of vectors in a basis for $V$ is called the **dimension** of $V$, denoted as $\text{dim}(V)$.

## Definitions:

1. **Linear Independence**: A set of vectors $v_1, v_2,\ldots, v_n\in V$ is linearly independent if the only way to write the zero vector as a linear combination of these vectors is by taking all coefficients to be zero. In other words, $\alpha_1 v_1+\alpha_2 v_2+\ldots+\alpha_n v_n= 0$ implies $\alpha_1=\alpha_2=\ldots=\alpha_n= 0$.

2. **Span**: The span of a set of vectors $S$ is the set of all possible linear combinations of the vectors in $S$. If the span of a set of vectors equals the vector space $V$, then we say that the set **spans** $V$.

## Examples:

1. Consider $\mathbb{R}^3$, the vector space of all 3-dimensional real vectors. The standard basis for $\mathbb{R}^3$ is $\{(1, 0, 0),(0, 1, 0),(0, 0, 1)\}$. Any vector in $\mathbb{R}^3$ can be uniquely written as a linear combination of these basis vectors.

2. The vectors $\{(1, 1),(1,-1)\}$ form a basis for $\mathbb{R}^2$. They are linearly independent and span all of $\mathbb{R}^2$.

## Historical Context:
The development of the theory of bases and dimension can be traced back to the early 19th century, with significant contributions from mathematicians such as Carl Friedrich Gauss and Georg Friedrich Bernhard Riemann. The concept of bases and dimension plays a fundamental role in various branches of mathematics, including linear algebra, functional analysis, and geometry.

## Real-life Example:
Imagine a plane in three-dimensional space. Any point on the plane can be uniquely identified by two vectors in the directions of two non-parallel lines on the plane. These two vectors could form a basis for the plane.

## Exam Questions:

1. Given the vectors $v_1=(1, 2, 3)$ and $v_2=(2, 1,-1)$ in $\mathbb{R}^3$, determine if they form a basis for $\mathbb{R}^3$.
    
2. Prove that any two vectors in $\mathbb{R}^2$ that are not scalar multiples of each other form a basis for $\mathbb{R}^2$.
   
3. If a vector space $V$ has dimension 4 and contains a set of 5 linearly independent vectors, is this set a basis for $V$? Justify your answer.