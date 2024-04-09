# Linear Combinations and Spanning Sets

Linear combinations and spanning sets are fundamental concepts in linear algebra that play a crucial role in understanding vector spaces and their subspaces. They provide a foundation for solving systems of linear equations, studying transformations, and much more.

## Definitions

### Linear Combination
Given vectors $\mathbf{v}_1,\mathbf{v}_2,\ldots,\mathbf{v}_n$ in a vector space $V$ over a field $F$, a *linear combination* of these vectors is an expression of the form $c_1\mathbf{v}_1+ c_2\mathbf{v}_2+\ldots+ c_n\mathbf{v}_n$, where $c_1, c_2,\ldots, c_n\in F$. The scalars $c_1, c_2,\ldots, c_n$ are called the *coefficients* of the linear combination.

### Spanning Set
A set of vectors $\{\mathbf{v}_1,\mathbf{v}_2,\ldots,\mathbf{v}_n\}$ in a vector space $V$ is said to *span* $V$ if every vector in $V$ can be expressed as a linear combination of $\mathbf{v}_1,\mathbf{v}_2,\ldots,\mathbf{v}_n$. In other words, $V$ is the smallest subspace of $V$ containing $\mathbf{v}_1,\mathbf{v}_2,\ldots,\mathbf{v}_n$.

## Explanation
- **Linear Combinations**: The concept of a linear combination allows us to generate new vectors by scaling and adding existing vectors. It forms the building block for understanding the properties of vector spaces and subspaces.
  
- **Spanning Sets**: A spanning set is a set of vectors that, when combined in different linear combinations, can reach every point in a vector space. They provide a way to describe and understand the structure and dimensionality of a vector space.

### Real-life Example
Imagine a two-dimensional plane in space. The vectors $\mathbf{i}=\begin{pmatrix} 1\\ 0\end{pmatrix}$ and $\mathbf{j}=\begin{pmatrix} 0\\ 1\end{pmatrix}$ form a spanning set for this plane. Any point on the plane can be reached by scaling and adding $\mathbf{i}$ and $\mathbf{j}$.

## Historical Context
The concept of linear combinations and spanning sets has a rich history dating back to the early developments of linear algebra. Mathematicians like Leonhard Euler, Carl Friedrich Gauss, and Augustin-Louis Cauchy made significant contributions to understanding vector spaces and their properties, laying the groundwork for the modern theory of linear algebra.

## Exam Questions
1. Let $\mathbf{v}_1=\begin{pmatrix} 1\\ 2\end{pmatrix}$ and $\mathbf{v}_2=\begin{pmatrix} 3\\ 4\end{pmatrix}$. Determine if the vector $\begin{pmatrix} 5\\ 6\end{pmatrix}$ is a linear combination of $\mathbf{v}_1$ and $\mathbf{v}_2$.
   
2. Show that the set of vectors $\{\begin{pmatrix} 1\\ 0\end{pmatrix},\begin{pmatrix} 0\\ 1\end{pmatrix}\}$ spans the entire two-dimensional Euclidean space.

3. Discuss the relationship between linear combinations and spanning sets in the context of subspaces of vector spaces.

By understanding the concepts of linear combinations and spanning sets, mathematicians can analyze the structure of vector spaces, solve systems of equations, and study transformations in various mathematical applications.