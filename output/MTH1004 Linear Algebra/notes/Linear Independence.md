# Linear Independence

## Definition
A set of vectors $\mathbf{v_1},\mathbf{v_2},\ldots,\mathbf{v_n}$ in a vector space is said to be **linearly independent** if there exist constants $c_1, c_2,\ldots, c_n$ not all zero, such that:

$$c_1\mathbf{v_1}+ c_2\mathbf{v_2}+\ldots+ c_n\mathbf{v_n}=\mathbf{0},$$

where $\mathbf{0}$ is the zero vector. If such constants do not exist, the set of vectors is said to be **linearly dependent**.

## Explanation
Linear independence is a fundamental concept in linear algebra. Intuitively, a set of vectors is linearly independent if none of the vectors in the set can be written as a linear combination of the others. In other words, no vector in the set is redundant, and each vector contributes uniquely to the span of the set.

For example, in $\mathbb{R}^2$, the vectors $\begin{pmatrix} 1\\ 0\end{pmatrix}$ and $\begin{pmatrix} 0\\ 1\end{pmatrix}$ form a linearly independent set because there are no non-zero constants $c_1$ and $c_2$ such that $c_1\begin{pmatrix} 1\\ 0\end{pmatrix}+ c_2\begin{pmatrix} 0\\ 1\end{pmatrix}=\begin{pmatrix} 0\\ 0\end{pmatrix}$.

In contrast, the vectors $\begin{pmatrix} 1\\ 1\end{pmatrix}$ and $\begin{pmatrix} 2\\ 2\end{pmatrix}$ in $\mathbb{R}^2$ are linearly dependent because $2\begin{pmatrix} 1\\ 1\end{pmatrix}-\begin{pmatrix} 2\\ 2\end{pmatrix}=\begin{pmatrix} 0\\ 0\end{pmatrix}$.

## Historical Context
The concept of linear independence was first formalized by the German mathematician Hermann Grassmann in the 19th century as part of his work on vector spaces and multilinear algebra. Linear independence forms a cornerstone of modern linear algebra and is essential in various mathematical and scientific disciplines.

## Real-life Examples
1. **Economics**: In economics, linear independence is crucial for understanding input-output relationships in production processes. If the input factors are linearly dependent, it implies some redundancy in the production process.
   
2. **Engineering**: Linear independence plays a significant role in structural engineering to determine the stability and rigidity of architectural frameworks. Linearly dependent forces can lead to structural instability.
   
3. **Data Analysis**: In machine learning, linear independence is essential for feature selection and dimensionality reduction techniques. Linearly dependent features can introduce multicollinearity issues in predictive models.

## Exam Questions
1. Determine whether the vectors $\begin{pmatrix} 1\\ 2\end{pmatrix}$, $\begin{pmatrix} 3\\ 1\end{pmatrix}$, and $\begin{pmatrix} 6\\ 4\end{pmatrix}$ in $\mathbb{R}^2$ are linearly dependent or independent.
   
2. Explain the significance of linear independence in the context of solving systems of linear equations.
   
3. Provide an example from a real-world scenario where linear independence is a critical concept for analysis.