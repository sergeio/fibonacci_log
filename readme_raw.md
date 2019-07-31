Fibonacci
---------

_There's a logarithmic-time solution?!_


### Background

If you just needed code that generates the nth Fibonacci number, a trivial
implementation might look something like this:

```python
def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)
```
`fib_triv.py`

If you've never seen recursion before, this is kind of magical.  But once the
novelty wears off, you notice that generating the 100th Fibonacci number is
basically impossible because the runtime is exponential.

![exponential runtime graph](plot_trivial_timing.png)

With a little bit of cleverness, we can code a linear-ish solution:

```python
def fib(n):
    if n < 2:
        return 1
    low = 1
    high = 1
    for _ in xrange(n - 1):
        low, high = high, low + high
    return high
```
`fib_lin.py`

If you've spent some time with programming interview questions, you might also
know that there's a basically [constant-time solution](https://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression),
if you have a bunch of extra square-roots-of-five lying around.


### Logarithmic-time

What I didn't know until recently is that there also exists a
logarithmic-ish-time solution.

The first bit of knowledge we need is that it is possible to represent the
operation of transforming a Fibonacci number into the next Fibonacci number
as a single matrix multiplication.

Specifically, if we take the column vector
$ f = \begin{bmatrix}
    F_{n-1} F_n
   \end{bmatrix}
$, and left-multiply it by

$
A = \begin{bmatrix}
    0 & 1
    1 & 1
\end{bmatrix}
$

then the resulting vector will be
$ f\prime = \begin{bmatrix}
    F_{n} F_{n+1}
   \end{bmatrix}
$.

($F_{n-1}$ is the n-1th Fibonacci number, $F_n$ is the nth and $F_{n+1}$ is the
n+1th)

So we have $A \cdot f = f\prime$.

And it follows that if we want to advance in the sequence by two, we can just
multiply by A twice:

$ A \cdot A \cdot f = A \cdot f\prime = f\prime\prime $

$ A^2 \cdot f = f\prime\prime $

More generally, we can say that $ A^n * f $ will advance the sequence by n.

And from here, all we need is a method that computes A^n in logarithmic time to
get a logarithmic-time Fibonacci number generator.  The bit of intuition that
allows us to do this is that in order to compute e.g. $ 2^16 $, we don't need
to multiply 2 by itself 16 times.  We can rely on the fact that $ 2^16 = 2^8 *
2^8 $.
[Wikipedia](https://en.wikipedia.org/wiki/Exponentiation_by_squaring) has more.

See `fib_log.py` if you're curious.


### Let's time some things

If we run the code in `timing.py`, we can see that indeed the logarithmic
solution outperforms the linear on on a large-enough scale by quite a bit:

![exponential runtime graph](plot_linear_log_10k.png)


If we restrict the sequence to just the first 2000 numbers, the runtime looks
even more logarithmic:

![exponential runtime graph](plot_linear_log_2k.png)

Some of the jitter is just noise, and some of it is due to the fact that
calculating powers of two takes fewer operations with our
exponentiation-by-squaring method.

The other thing of note here, and the reason I've said logarithmic-ish and
linear-ish so many times here, is that while the number of operations is indeed
linear or logarithmic, the time those operations take is not.  You can clearly
see that while the orange algorithm is labeled as "fib_lin", the runtime
clearly curves upward.  And that's because the 10,000th Fibonacci number is
well over 2,000 digits long.  Adding and multiplying such big numbers takes
more CPU cycles; timing depends on the magnitudes of the numbers.