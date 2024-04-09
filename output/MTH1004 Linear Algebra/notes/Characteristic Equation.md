# Characteristic Equation

In mathematics, the characteristic equation is a fundamental concept that arises in various fields, such as linear algebra and differential equations. It is used to find eigenvalues or characteristic roots of a square matrix or a differential equation.

## Eigenvalues and Eigenvectors

Let's first consider the characteristic equation in the context of linear algebra. Given an $ n\times n$ square matrix $ A$, the characteristic equation is defined as:

$$\text{det}(A-\lambda I)= 0$$

where $\lambda$ is an eigenvalue, $ I$ is the identity matrix of the same size as $ A$, and $\text{det}$ denotes the determinant. Solving this equation yields the eigenvalues of the matrix $ A$.

The corresponding eigenvectors are the non-zero vectors $ v$ satisfying the equation:

$$ A v=\lambda v$$

where $\lambda$ is an eigenvalue. Eigenvectors are essential as they represent the directions in which a linear transformation represented by the matrix stretches or compresses.

## Example

Consider the matrix:

$$ A=\begin{pmatrix} 2& 1\\ 1& 2\end{pmatrix}$$

To find the eigenvalues, we solve the characteristic equation:

$$\text{det}\left(\begin{pmatrix} 2& 1\\ 1& 2\end{pmatrix}-\lambda\begin{pmatrix} 1& 0\\ 0& 1\end{pmatrix}\right)= 0$$

$$\text{det}\left(\begin{pmatrix} 2-\lambda& 1\\ 1& 2-\lambda\end{pmatrix}\right)= 0$$

$$(2-\lambda)^2- 1= 0\Rightarrow\lambda^2- 4\lambda+ 3= 0$$

Solving the quadratic equation gives us the eigenvalues $\lambda_1= 3$ and $\lambda_2= 1$.

## Historical Context

The concept of eigenvalues and eigenvectors, which are closely related to the characteristic equation, was introduced by the German mathematician David Hilbert in 1904. This concept has found applications in various scientific fields, including physics, engineering, and computer science.

## Application in Differential Equations

In the context of differential equations, the characteristic equation plays a crucial role in solving linear differential equations. For a linear differential equation of order $ n$ with constant coefficients, the characteristic equation is given by:

$$ a_n r^n+ a_{n-1} r^{n-1}+\cdots+ a_1 r+ a_0= 0$$

where $ r$ is the unknown variable and the $ a_i$'s are the coefficients of the differential equation. The roots of this characteristic equation help in determining the general solution of the differential equation.

## Real-life Example

An application of the characteristic equation can be found in structural engineering when analysing the stability of a structure. By formulating the problem as a system of linear equations and finding the eigenvalues using the characteristic equation, engineers can determine the critical loadings that would cause the structure to buckle or deform.

## Exam Questions
1. Find the characteristic equation and determine the eigenvalues for the matrix $B=\begin{pmatrix} 4& 2\\ 2& 4\end{pmatrix}$.
2. Solve the characteristic equation for the differential equation $y''- 5y'+ 6y= 0$ and find the roots.
3. Explain the significance of eigenvalues and eigenvectors in the context of linear transformations.