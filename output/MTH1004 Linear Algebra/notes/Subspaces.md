# Subspaces

In linear algebra, a **subspace** of a vector space $V$ is a subset of $V$ that is itself a vector space with respect to the operations of addition and scalar multiplication defined on $V$. More formally, let $V$ be a vector space over a field $\mathbb{F}$. A subset $W$ of $V$ is a subspace of $V$ if:

1. The zero vector of $V$ is in $W$.
2. For all vectors $v, w\in W$, the sum $v+ w$ is in $W$.
3. For all vectors $v\in W$ and scalars $c\in\mathbb{F}$, the scalar multiple $cv$ is in $W$.

## Examples

1. Consider the vector space $\mathbb{R}^3$. The $xy$-plane, defined as the set of all vectors of the form $(x, y, 0)$, is a subspace of $\mathbb{R}^3$.
2. The set of all polynomials of degree at most $n$, denoted by $P_n(\mathbb{R})$, is a subspace of the vector space of all polynomials over $\mathbb{R}$.

## Historical Context

The concept of subspaces has its roots in the development of linear algebra, dating back to the 19th century. The pioneering work of mathematicians like Carl Friedrich Gauss, Augustin-Louis Cauchy, and Hermann Grassmann laid the foundation for understanding vector spaces and their subspaces. The formal definition and properties of subspaces were further elucidated by mathematicians such as David Hilbert and Emmy Noether in the early 20th century.

## Real-life Applications

Subspaces find applications in various fields such as computer graphics, control theory, and statistics. In computer graphics, subspaces are used to represent transformations and projections of objects in three-dimensional space. In control theory, subspaces help in analyzing the stability and controllability of dynamical systems. In statistics, subspaces are employed in principal component analysis and linear regression to model relationships between variables.

## Exam Questions

1. Prove that the set of all solutions to a homogeneous system of linear equations forms a subspace of the vector space of all solutions to the corresponding non-homogeneous system.
2. Let $V$ be a vector space and $W_1, W_2$ be subspaces of $V$. Prove or disprove: $W_1\cup W_2$ is necessarily a subspace of $V$.
3. Consider the vector space $P(\mathbb{R})$ of all polynomials over $\mathbb{R}$. Let $W$ be the set of all polynomials of the form $a_0+ a_1x$ where $a_0, a_1\in\mathbb{R}$. Is $W$ a subspace of $P(\mathbb{R})$? Justify your answer.