# Symmetric Matrices

In linear algebra, a **symmetric matrix** is a square matrix that is equal to its transpose. Formally, an $n\times n$ matrix $A$ is symmetric if $A= A^\top$, where $A^\top$ denotes the transpose of matrix $A$. 

## Properties

1. The main diagonal of a symmetric matrix consists of real numbers.
2. The eigenvalues of a symmetric matrix are real.
3. Symmetric matrices are always diagonalizable.
4. The sum of two symmetric matrices is symmetric, and the product of two symmetric matrices need not be symmetric.

## Examples

Consider the following symmetric matrix:
$$
A=\begin{pmatrix}
2&-1& 0\\-1& 3& 2\\
0& 2& 1\end{pmatrix}$$
This matrix is symmetric because $A= A^\top$.

Another example is the identity matrix $I_n$, which is always symmetric since it equals its transpose.

## Applications

Symmetric matrices have various applications in mathematics and real-life scenarios. For instance, in physics, the moment of inertia matrix of a rigid body is always symmetric. In statistics, the covariance matrix of a multivariate normal distribution is symmetric. Additionally, in graph theory, the adjacency matrix of an undirected graph is symmetric.

## Historical Context

The study of symmetric matrices dates back to the 18th century when Euler introduced the concept of quadratic forms. However, the modern understanding and manipulation of symmetric matrices were significantly developed in the 19th and 20th centuries with advancements in linear algebra and matrix theory.

## Exam Questions

1. Prove that the eigenvalues of a symmetric matrix are real.
2. Show that the sum of two symmetric matrices is always symmetric.
3. Consider a real symmetric matrix $A$. Prove that there exists an orthogonal matrix $P$ such that $P^\top AP$ is a diagonal matrix.