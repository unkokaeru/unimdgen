# Matrix Operations

In linear algebra, a **matrix** is a rectangular array of numbers, symbols, or expressions, arranged in rows and columns. Matrices are fundamental in various mathematical disciplines and are widely used in fields such as physics, computer science, and engineering.

## Basic Definitions

### Matrix Representation

An $m\times n$ matrix is a rectangular array of numbers with $m$ rows and $n$ columns. A matrix can be represented as:

$$
A=\begin{bmatrix} a_{11}& a_{12}&\cdots& a_{1n}\\ a_{21}& a_{22}&\cdots& a_{2n}\\\vdots&\vdots&\ddots&\vdots\\ a_{m_{1}}& a_{m_{2}}&\cdots& a_{mn}\end{bmatrix}$$

where $a_{ij}$ represents the entry in the $i$th row and $j$th column of the matrix.

### Addition of Matrices

Given two matrices $A$ and $B$ of the same size, their sum $A+ B$ is computed by adding corresponding entries:

$$
A+ B=\begin{bmatrix} a_{11}+b_{11}& a_{12}+b_{12}&\cdots& a_{1n}+b_{1n}\\ a_{21}+b_{21}& a_{22}+b_{22}&\cdots& a_{2n}+b_{2n}\\\vdots&\vdots&\ddots&\vdots\\ a_{m_{1}}+b_{m_{1}}& a_{m_{2}}+b_{m_{2}}&\cdots& a_{mn}+b_{mn}\end{bmatrix}$$

### Scalar Multiplication

Multiplying a matrix $A$ by a scalar $k$ results in a new matrix denoted by $kA$, where each entry of $A$ is multiplied by $k$:

$$
kA=\begin{bmatrix} ka_{11}& ka_{12}&\cdots& ka_{1n}\\ ka_{21}& ka_{22}&\cdots& ka_{2n}\\\vdots&\vdots&\ddots&\vdots\\ ka_{m_{1}}& ka_{m_{2}}&\cdots& ka_{mn}\end{bmatrix}$$

### Multiplication of Matrices

For two matrices $A$ of size $m\times n$ and $B$ of size $n\times p$, their product $AB$ is defined if the number of columns in $A$ is equal to the number of rows in $B$. The resulting matrix $C= AB$ has size $m\times p$, and its entries are computed as follows:

$$
c_{ij}=\sum_{k=1}^{n} a_{ik}b_{kj}$$

## Applications and Real-Life Examples

Matrices are widely used in various real-world applications, such as:

- **Transformations**: Matrices are used to represent transformations in computer graphics and robotics. For example, a 2D transformation matrix can rotate, scale, or translate an object on a plane.
  
- **Networks**: Matrices are used to model and analyze networks in graph theory and computer science. The adjacency matrix of a graph can provide valuable insights into its structure.
  
- **Economics**: Input-output matrices are used in economics to model the interdependencies between different sectors of an economy.

## Historical Context

Matrices were first introduced by James Joseph Sylvester in the mid-19th century. However, their systematic study and application were significantly developed by the mathematician Arthur Cayley.

## Exam Questions

1. Given matrices $A=\begin{bmatrix} 1& 2\\ 3& 4\end{bmatrix}$ and $B=\begin{bmatrix} 5& 6\\ 7& 8\end{bmatrix}$, calculate $A+ B$.
2. Let $A=\begin{bmatrix} 2& 4\\ 6& 8\end{bmatrix}$ and $k= 3$. Compute $kA$.
3. Determine if it is possible to multiply matrices $C$ and $D$ where $C=\begin{bmatrix} 1& 2\\ 3& 4\end{bmatrix}$ and $D=\begin{bmatrix} 5& 6& 7\\ 8& 9& 10\end{bmatrix}$.

Remember to simplify your answers as much as possible.