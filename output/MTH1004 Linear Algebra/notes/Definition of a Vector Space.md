# Vector Space

A **vector space** over a field $\mathbb{F}$ is a set $V$ equipped with two operations: vector addition and scalar multiplication, satisfying a set of properties. 

More formally, a vector space is a triple $(V,+,\cdot)$ where:
- $V$ is a set of objects called vectors.
- $+$ is an operation called vector addition, which takes two vectors $u, v\in V$ and produces a vector $u+ v\in V$.
- $\cdot$ is an operation called scalar multiplication, which takes a scalar $\alpha\in\mathbb{F}$ and a vector $v\in V$ and produces a vector $\alpha\cdot v\in V$.

These operations must satisfy the following properties for all $u, v, w\in V$ and all scalars $\alpha,\beta\in\mathbb{F}$:
1. **Closure under addition:** $u+ v\in V$.
2. **Associativity of addition:** $(u+ v)+ w= u+(v+ w)$.
3. **Commutativity of addition:** $u+ v= v+ u$.
4. **Existence of additive identity:** There exists a vector $\mathbf{0}\in V$ such that $v+\mathbf{0}= v$ for all $v\in V$.
5. **Existence of additive inverse:** For every $v\in V$, there exists a vector $-v\in V$ such that $v+(-v)=\mathbf{0}$.
6. **Closure under scalar multiplication:** $\alpha\cdot v\in V$.
7. **Distributivity of scalar sums:** $(\alpha+\beta)\cdot v=\alpha\cdot v+\beta\cdot v$.
8. **Distributivity of vector sums:** $\alpha\cdot(u+ v)=\alpha\cdot u+\alpha\cdot v$.
9. **Compatibility of scalar multiplication with field multiplication:** $(\alpha\beta)\cdot v=\alpha\cdot(\beta\cdot v)$.
10. **Identity element of scalar multiplication:** $1\cdot v= v$, where $1$ is the multiplicative identity in $\mathbb{F}$.

## Historical Context
The concept of a vector space was introduced by Hermann Grassmann in the 19th century as part of his development of the theory of multilinear algebra. The abstract notion of a vector space has since become a fundamental concept in mathematics with numerous applications in various branches, including linear algebra, functional analysis, and differential geometry.

## Real-life Example
Consider a three-dimensional Euclidean space $\mathbb{R}^3$. The set of all vectors in $\mathbb{R}^3$ forms a vector space over the field of real numbers. Here, vector addition corresponds to adding individual components of vectors, and scalar multiplication involves multiplying each component of a vector by a real number.

## Exam Questions
1. Prove that the additive identity in a vector space is unique.
2. Show that the set of all polynomials of degree at most $n$ forms a vector space over the field of real numbers.
3. Given two vectors $\mathbf{u}=\begin{pmatrix} 2\\-1\end{pmatrix}$ and $\mathbf{v}=\begin{pmatrix} 3\\ 4\end{pmatrix}$ in $\mathbb{R}^2$, find the vector that represents $2\mathbf{u}-\frac{1}{2}\mathbf{v}$.