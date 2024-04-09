# Limits of Functions

In calculus, the concept of limits plays a crucial role in understanding how functions behave near a particular point. When we talk about the limit of a function as it approaches a certain point, we are essentially interested in the value that the function approaches as the input gets closer and closer to that point.

## Definition

Let $f(x)$ be a function defined in some open interval containing $x=a$, except possibly at $x=a$. The **limit of $f(x)$ as $x$ approaches $a$**, denoted by $\lim_{x\to a} f(x)$, is the value that $f(x)$ approaches as $x$ gets arbitrarily close to $a$. Formally, we say $\lim_{x\to a} f(x)= L$ if for every $\varepsilon> 0$, there exists a $\delta> 0$ such that if $0<|x- a|<\delta$, then $|f(x)- L|<\varepsilon$.

## Example

Consider the function $f(x)=\frac{x^2- 1}{x- 1}$. If we evaluate $f(x)$ at $x= 1$, we get an indeterminate form $\frac{0}{0}$. However, by simplifying the function, we find that $f(x)= x+ 1$ for all $x\neq 1$. Therefore, $\lim_{x\to 1} f(x)= 2$.

## Historical Context

The concept of limits has a rich historical background. Mathematicians such as Newton, Leibniz, and Cauchy made significant contributions to the development of calculus and the understanding of limits. One can think of the limit concept as the gateway to calculus, as it underpins the definitions of derivatives and integrals.

## Real-life Applications

Limits are not just theoretical ideas; they have practical applications in real life. For instance, in physics, limits are used to define instantaneous velocity and acceleration. In economics, limits help in calculating marginal cost and revenue. Engineering relies on limits for designing structures that can withstand extreme conditions.

## Exam Questions

1. Compute the limit: $\lim_{x\to 2}\frac{x^2- 4}{x- 2}$.
2. Determine if the limit $\lim_{x\to 0}\frac{\sin(x)}{x}$ exists. Justify your answer.
3. Given the function $g(x)=\begin{cases} x+ 1,&\text{if} x< 2\\ 3x- 1,&\text{if} x\geq 2\end{cases}$, find $\lim_{x\to 2} g(x)$.

Remember, understanding limits is crucial in calculus as they form the foundation for more advanced topics like derivatives and integrals.