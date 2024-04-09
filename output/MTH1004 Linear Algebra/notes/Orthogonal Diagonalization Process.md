# Orthogonal Diagonalization Process

In linear algebra, the orthogonal diagonalization process is a fundamental technique used to diagonalize a symmetric matrix. Diagonalization refers to the process of finding a diagonal matrix that is similar to the given matrix. When dealing with symmetric matrices, which are square matrices that are equal to their transpose, we can further diagonalize them using an orthogonal matrix.

## Definitions:

- **Symmetric Matrix**: A square matrix $A$ is said to be symmetric if it is equal to its transpose, i.e., $A= A^T$.
  
- **Orthogonal Matrix**: A square matrix $Q$ is said to be orthogonal if its inverse is equal to its transpose, i.e., $Q^T= Q^{-1}$.

- **Diagonal Matrix**: A square matrix $D$ is said to be diagonal if all its off-diagonal entries are zero, i.e., $d_{ij}= 0$ for $i\neq j$.

## Explanation:

Given a symmetric matrix $A$, the orthogonal diagonalization process involves finding an orthogonal matrix $Q$ and a diagonal matrix $D$ such that $A= QDQ^T$. The columns of $Q$ are the orthonormal eigenvectors of $A$, and the diagonal entries of $D$ are the corresponding eigenvalues.

1. **Find the Eigenvalues and Eigenvectors**: Determine the eigenvalues of $A$ by solving the characteristic equation $|A-\lambda I|= 0$, where $\lambda$ represents the eigenvalue. Then, find the eigenvectors corresponding to each eigenvalue.

2. **Construct the Orthogonal Matrix**: Form the orthogonal matrix $Q$ by normalizing the eigenvectors found in the previous step. Since the eigenvectors are orthogonal, normalizing them will make them orthonormal.

3. **Construct the Diagonal Matrix**: Once $Q$ is formed, the matrix $D$ can be constructed by placing the eigenvalues along the diagonal in the same order as the corresponding eigenvectors in $Q$.

4. **Verify the Diagonalization**: Finally, verify that $A= QDQ^T$ to ensure that the orthogonal diagonalization process was successful.

The orthogonal diagonalization process is not only useful in theoretical mathematics but also finds applications in various fields such as physics, engineering, and computer science.

## Example:

Consider the symmetric matrix:
$$A=\begin{bmatrix} 1& 2\\ 2& 4\end{bmatrix}.$$

1. **Find Eigenvalues and Eigenvectors**:
    - Solving $|A-\lambda I|= 0$, we find the eigenvalues $\lambda_1= 0$ and $\lambda_2= 5$.
    - Corresponding eigenvectors are $v_1=\begin{bmatrix}-2\\ 1\end{bmatrix}$ and $v_2=\begin{bmatrix} 1\\ 2\end{bmatrix}$.

2. **Construct $Q$ and $D$**:
    - $Q=\begin{bmatrix}-2/\sqrt{5}& 1/\sqrt{5}\\ 1/\sqrt{5}& 2/\sqrt{5}\end{bmatrix}$ is the orthogonal matrix.
    - $D=\begin{bmatrix} 0& 0\\ 0& 5\end{bmatrix}$ is the diagonal matrix.

3. **Verify the Diagonalization**:
    - $A= QDQ^T=\begin{bmatrix} 1& 2\\ 2& 4\end{bmatrix}$.

## Exam Questions:

1. Diagonalize the following symmetric matrix using the orthogonal diagonalization process:
$$B=\begin{bmatrix} 3& 1\\ 1& 3\end{bmatrix}.$$

2. Explain the significance of symmetric matrices in the context of diagonalization.

3. How does the orthogonal diagonalization process differ from the regular diagonalization process?