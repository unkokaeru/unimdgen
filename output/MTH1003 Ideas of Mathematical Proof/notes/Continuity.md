# Continuity

In mathematics, continuity is a fundamental concept that describes the behavior of functions. Intuitively, a function is continuous if its graph can be drawn without lifting the pencil from the paper. More formally, a function $f:\mathbb{R}\rightarrow\mathbb{R}$ is said to be continuous at a point $a$ in its domain if for every $\varepsilon> 0$, there exists a $\delta> 0$ such that for all $x$ satisfying $|x- a|<\delta$, we have $|f(x)- f(a)|<\varepsilon$.

### Formal Definition

Let $f:\mathbb{R}\rightarrow\mathbb{R}$ be a function and $a$ be a point in its domain. The function $f$ is continuous at $a$ if $\lim_{x\to a} f(x)= f(a)$.

### Types of Continuity

1. **Continuity at a Point**: A function $f$ is continuous at a point $a$ if $\lim_{x\to a} f(x)= f(a)$.
2. **Continuity on an Interval**: A function $f$ is continuous on an interval $I$ if it is continuous at every point in that interval.
3. **Uniform Continuity**: A function $f$ is uniformly continuous on a set $A$ if for every $\varepsilon> 0$, there exists a $\delta> 0$ such that for all $x, y\in A$ satisfying $|x- y|<\delta$, we have $|f(x)- f(y)|<\varepsilon$.

### Examples

1. The function $f(x)= 2x+ 3$ is continuous everywhere.
2. The function $g(x)=\frac{1}{x}$ is continuous on its domain $(-\infty, 0)\cup(0,\infty)$.
3. The function $h(x)=\sqrt{x}$ is continuous on its domain $[0,\infty)$.

### Historical Context

The concept of continuity has a long and rich history dating back to ancient Greeks. The mathematician and philosopher, Eudoxus of Cnidus, introduced the method of exhaustion to define and work with continuous quantities. This idea laid the foundation for the development of calculus by Newton and Leibniz in the 17th century.

### Real-life Example

Imagine a car moving along a straight road. The position of the car at any time $t$ can be described by a continuous function of time. If the function representing the position of the car were not continuous, it would imply abrupt jumps or discontinuities in the car's motion, which is physically unrealistic.

### Exam Questions

1. Define continuity of a function at a point and illustrate with an example.
2. Discuss the difference between continuity at a point and continuity on an interval.
3. Prove or disprove that the function $f(x)=\sin(x)$ is uniformly continuous on its domain $[0, 2\pi]$.

Remember, understanding the concept of continuity is crucial in various branches of mathematics, especially in analysis and calculus.