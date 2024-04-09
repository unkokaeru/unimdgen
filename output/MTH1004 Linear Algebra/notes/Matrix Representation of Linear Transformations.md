# Matrix Representation of Linear Transformations

In linear algebra, a **linear transformation** is a function between two vector spaces that preserves vector addition and scalar multiplication. One of the fundamental concepts in linear algebra is representing a linear transformation as a matrix. This allows us to perform computations involving linear transformations using matrix operations.

## Definitions

### Linear Transformation
Let $V$ and $W$ be vector spaces over a field $\mathbb{F}$. A function $T: V\to W$ is called a **linear transformation** if it satisfies the following properties for all vectors $\mathbf{v}_1,\mathbf{v}_2\in V$ and all scalars $c\in\mathbb{F}$:
1. $T(\mathbf{v}_1+\mathbf{v}_2)= T(\mathbf{v}_1)+ T(\mathbf{v}_2)$ (additivity)
2. $T(c\mathbf{v}_1)= cT(\mathbf{v}_1)$ (homogeneity)

### Matrix Representation
Let $T:\mathbb{R}^n\to\mathbb{R}^m$ be a linear transformation. The **matrix representation** of $T$ with respect to standard bases is an $m\times n$ matrix $A$ such that for any vector $\mathbf{v}\in\mathbb{R}^n$, the vector $T(\mathbf{v})$ can be computed as $A\mathbf{v}$.

## Finding the Matrix Representation

Given a linear transformation $T:\mathbb{R}^n\to\mathbb{R}^m$, the matrix representation $A$ of $T$ can be found by considering the images of the standard basis vectors in $\mathbb{R}^n$. If $\mathbf{e}_1,\mathbf{e}_2,\ldots,\mathbf{e}_n$ are the standard basis vectors in $\mathbb{R}^n$, then the $j$th column of the matrix $A$ is given by $T(\mathbf{e}_j)$.

## Example

Consider the linear transformation $T:\mathbb{R}^2\to\mathbb{R}^2$ defined by $T\left(\begin{pmatrix} x\\ y\end{pmatrix}\right)=\begin{pmatrix} 2x+y\\ x-3y\end{pmatrix}$. Let's find the matrix representation of $T$.

We compute $T\left(\begin{pmatrix} 1\\ 0\end{pmatrix}\right)=\begin{pmatrix} 2\\ 1\end{pmatrix}$ and $T\left(\begin{pmatrix} 0\\ 1\end{pmatrix}\right)=\begin{pmatrix} 1\\-3\end{pmatrix}$. Therefore, the matrix representation of $T$ is $A=\begin{pmatrix} 2& 1\\ 1&-3\end{pmatrix}$.

## Historical Context

The concept of matrix representation of linear transformations has its roots in the works of mathematicians such as Emmy Noether and David Hilbert in the early 20th century. Their contributions to abstract algebra and linear algebra laid the foundation for the systematic study of linear transformations and their matrix representations.

## Real-life Applications

Matrix representation of linear transformations finds wide applications in various fields such as computer graphics, physics, and engineering. For example, in computer graphics, transformations like translation, rotation, and scaling of objects are efficiently represented and manipulated using matrices.

## Exam Questions

1. Define a linear transformation between vector spaces and explain the properties it must satisfy.
2. Given a linear transformation $T:\mathbb{R}^3\to\mathbb{R}^2$, how would you find its matrix representation?
3. Discuss the historical significance of matrix representations of linear transformations in the development of linear algebra.