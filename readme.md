Fibonacci
---------

_There's a logarithmic-time solution?!_

> Note: when I talk about linear-time, logarithmic-time, etc .. I really mean
> linear-number-of-operations.  Not all arithmetic operations run in constant
> time.

### Background

If you just needed code that generates the nth Fibonacci number, a trivial
implementation might look something like this:

```python
# fib_triv.py

def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)
```

If you've never seen recursion before, this is kind of magical.  But once the
novelty wears off, you notice that generating the 100th Fibonacci number is
basically impossible because the runtime is exponential.

![exponential runtime graph](plot_trivial_timing.png)

With a little bit of cleverness, we can code a linear time solution:

```python
# fib_lin.py

def fib(n):
    if n < 2:
        return 1
    low = 1
    high = 1
    for _ in xrange(n - 1):
        low, high = high, low + high
    return high
```

If you've spent some time with programming interview questions, you might also
know that there's a [constant-time solution](https://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression).


### Logarithmic-time

What I didn't know until recently is that there also exists a logarithmic-time
solution.

Let's represent the Fibonacci sequence as

<p align="center"><img src="svgs/0e60556f7e0512e10e2a4e6f40374a1d.svg" align=middle width=247.62045pt height=16.438356pt/></p>

The first bit of knowledge we need is that it is possible to represent the
operation of transforming a Fibonacci number into the next Fibonacci number
as a single matrix multiplication.

Specifically, if we take the column vector
<img src="svgs/bcaea708820e40ff046597c3047ba13e.svg" align=middle width=85.43205pt height=47.67147pt/>, and left-multiply it by
<img src="svgs/d42058db8b2e945862970c8cd520f879.svg" align=middle width=84.474885pt height=47.67147pt/>

then the resulting vector will be
<img src="svgs/f83e21e74ccfd55219d4de7c7b17cb58.svg" align=middle width=89.86131pt height=47.67147pt/>.

So we have <img src="svgs/f1e1a5b3bad54eb90cc6094d34559a97.svg" align=middle width=69.54321pt height=24.71634pt/>.

If it's been a while since you've done matrix multiplication, here's a
refresher, courtesy of
[matrixmultiplication.xyz](http://matrixmultiplication.xyz):

![matrix multiplication animation](matrix_multiplication_example.gif)


And it follows that if we want to advance in the sequence by two, we can just
multiply by A twice:

<p align="center"><img src="svgs/45139aa4427dc9ad494979426d787785.svg" align=middle width=158.081715pt height=16.3763325pt/></p>

<p align="center"><img src="svgs/7c25f8d85c1fbfc980ad332a998455c7.svg" align=middle width=80.707605pt height=17.399085pt/></p>


More generally, we can say that <img src="svgs/e0b84a42ef5d3070707127df0dda099e.svg" align=middle width=42.966165pt height=22.83138pt/> will advance the sequence by n.

Because exponentiation can be done in logarithmic time, we can now generate
Fibonacci numbers with matching time complexity.

The bit of intuition that allows us to do this is that in order to compute e.g.
<img src="svgs/d92a2953441d94f69056feca0851fe02.svg" align=middle width=21.324435pt height=26.76201pt/>, we don't need to multiply 2 by itself 16 times.  We can rely on the
fact that <img src="svgs/3a2fd667b3576501cdef833219cfbf26.svg" align=middle width=106.392495pt height=26.76201pt/>.  Similarly, <img src="svgs/91dda47546340477a65500096e2c5564.svg" align=middle width=14.77179pt height=26.76201pt/> can be
expressed as <img src="svgs/5b5a4b6381e075a4fede3fa7f32dba26.svg" align=middle width=42.237525pt height=26.76201pt/>.  Fully reduced, we can write
<img src="svgs/2aef0a4ad0ce23d12ed6df228346661d.svg" align=middle width=146.712225pt height=26.76201pt/>.  Instead of 16 multiplications, we
only need to do 5.
[Wikipedia](https://en.wikipedia.org/wiki/Exponentiation_by_squaring) has more.

See `fib_log.py` if you're curious.


### Let's time some things

If we run the code in `timing.py`, we can see that indeed the logarithmic
solution outperforms the linear on on a large-enough scale:

![exponential runtime graph](plot_linear_log_2k.png)

Some of the jitter is just noise, and some of it is due to the fact that
doing exponentiation where the exponent is a power of two takes fewer
operations with our exponentiation-by-squaring method.


Let's zoom out a bit more:

![exponential runtime graph](plot_linear_log_10k.png)

The reason I started this readme with a disclaimer is because while the number
of operations is indeed linear or logarithmic, the time those operations take
is not.  You can clearly see that while the orange algorithm is labeled as
`fib_linear`, the runtime clearly curves upward.  And that's because the
10,000th Fibonacci number is well over 2,000 digits long.  Adding and
multiplying such big numbers takes more CPU cycles; timing depends on the
magnitudes of the numbers.
