# Orthogonal Projection

In mathematics, the **orthogonal projection** is a fundamental concept in linear algebra that involves projecting a vector onto a subspace in such a way that the projected vector is orthogonal (perpendicular) to the subspace. The essence of orthogonal projection lies in decomposing a vector into two components - one component lying in the subspace and the other component being orthogonal to the subspace.

## Definitions:

### 1. Orthogonal Projection:

Let $V$ be a vector space with an inner product and $W$ be a subspace of $V$. For any vector $v$ in $V$, the **orthogonal projection** of $v$ onto $W$, denoted as $\text{proj}_{W} v$, is the closest vector in $W$ to $v$. It is obtained by finding the unique vector in $W$ that minimizes the distance from $v$.

### 2. Orthogonal Decomposition Theorem:

The **orthogonal decomposition theorem** states that for any vector $v$ in a vector space $V$ and a subspace $W\subset V$, there exist unique vectors $w\in W$ and $w^{\perp}\in W^{\perp}$ such that $v= w+ w^{\perp}$, where $w$ is the orthogonal projection of $v$ onto $W$ and $w^{\perp}$ is orthogonal to $W$.

### 3. Projection Matrix:

The **projection matrix** $P$ corresponding to the orthogonal projection onto a subspace $W$ can be defined as $P= A(A^{T}A)^{-1}A^{T}$, where $A$ is the matrix whose columns form a basis for $W$.

## Explanation:

Consider a real vector space $\mathbb{R}^{n}$ with an inner product $\langle\cdot,\cdot\rangle$. Let $W$ be a subspace of $\mathbb{R}^{n}$ with basis $\{\textbf{w}_1,\textbf{w}_2,\ldots,\textbf{w}_m\}$.

Given a vector $\textbf{v}$ in $\mathbb{R}^{n}$, the orthogonal projection of $\textbf{v}$ onto $W$, denoted as $\text{proj}_{W}\textbf{v}$, is computed as:

$$\text{proj}_{W}\textbf{v}=\sum_{i=1}^{m}\left(\frac{\langle\textbf{v},\textbf{w}_i\rangle}{\langle\textbf{w}_i,\textbf{w}_i\rangle}\right)\textbf{w}_i$$

The above formula essentially decomposes $\textbf{v}$ into a component lying in $W$ and a component orthogonal to $W$.

## Example:

Consider the subspace $W=\text{span}\left\{\begin{pmatrix} 1\\ 0\end{pmatrix},\begin{pmatrix} 0\\ 1\end{pmatrix}\right\}$ in $\mathbb{R}^{2}$. Let $\textbf{v}=\begin{pmatrix} 3\\ 2\end{pmatrix}$. We want to find the orthogonal projection of $\textbf{v}$ onto $W$.

The projection can be computed as:

$\text{proj}_{W}\textbf{v}=\left(\frac{\langle\textbf{v},\begin{pmatrix} 1\\ 0\end{pmatrix}\rangle}{\langle\begin{pmatrix} 1\\ 0\end{pmatrix},\begin{pmatrix} 1\\ 0\end{pmatrix}\rangle}\right)\begin{pmatrix} 1\\ 0\end{pmatrix}+\left(\frac{\langle\textbf{v},\begin{pmatrix} 0\\ 1\end{pmatrix}\rangle}{\langle\begin{pmatrix} 0\\ 1\end{pmatrix},\begin{pmatrix} 0\\ 1\end{pmatrix}\rangle}\right)\begin{pmatrix} 0\\ 1\end{pmatrix}$

Solving this gives $\text{proj}_{W}\textbf{v}=\begin{pmatrix} 3\\ 2\end{pmatrix}$.

## Historical Context:

The concept of orthogonal projection has its roots in the study of geometry and linear algebra. The idea of projecting one vector onto another or a subspace has been crucial in various mathematical applications, including physics, engineering, computer graphics, and optimization.

## Real-life Example:

Imagine a light source casting a shadow of an object onto the floor. The shadow represents the projection of the object onto the floor. In this case, the floor acts as the subspace onto which the object is projected, and the shadow is the orthogonal projection of the object onto the floor.

## Exam Questions:

1. Given a vector $\textbf{v}=\begin{pmatrix} 4\\ 5\\ 1\end{pmatrix}$ and a subspace $W$ spanned by $\begin{pmatrix} 1\\ 0\\ 0\end{pmatrix}$ and $\begin{pmatrix} 0\\ 1\\ 1\end{pmatrix}$ in $\mathbb{R}^{3}$, find the orthogonal projection of $\textbf{v}$ onto $W$.

2. Explain the significance of orthogonal projection in the context of least squares regression.

3. State and prove the orthogonal decomposition theorem for orthogonal projection onto a subspace in a real inner product space.