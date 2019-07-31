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
<img src="svgs/bcaea708820e40ff046597c3047ba13e.svg" align=middle width=85.43205pt height=47.67147pt/>, and left-multiply it by
<img src="svgs/d42058db8b2e945862970c8cd520f879.svg" align=middle width=84.474885pt height=47.67147pt/>

then the resulting vector will be
<img src="svgs/f83e21e74ccfd55219d4de7c7b17cb58.svg" align=middle width=89.86131pt height=47.67147pt/>.

(<img src="svgs/ee1c9fcc1452eff199fcb4bda04bc783.svg" align=middle width=35.52351pt height=22.46574pt/> is the n-1st Fibonacci number, <img src="svgs/c9c53a99901c4a67544997f70b0f01bc.svg" align=middle width=18.69681pt height=22.46574pt/> is the nth and <img src="svgs/b5fc1b39bc634786995c3b0ab5dd3809.svg" align=middle width=35.340855pt height=22.46574pt/> is the
n+1st)

So we have <img src="svgs/f1e1a5b3bad54eb90cc6094d34559a97.svg" align=middle width=69.54321pt height=24.71634pt/>.

And it follows that if we want to advance in the sequence by two, we can just
multiply by A twice:

<p align="center"><img src="svgs/45139aa4427dc9ad494979426d787785.svg" align=middle width=158.081715pt height=16.3763325pt/></p>

<p align="center"><img src="svgs/7c25f8d85c1fbfc980ad332a998455c7.svg" align=middle width=80.707605pt height=17.399085pt/></p>


More generally, we can say that <img src="svgs/e0b84a42ef5d3070707127df0dda099e.svg" align=middle width=42.966165pt height=22.83138pt/> will advance the sequence by n.

And from here, all we need is a method that computes <img src="svgs/925708a34751d898c4a6364dc7baaaa3.svg" align=middle width=20.454885pt height=22.46574pt/> in logarithmic
time to get a logarithmic-time Fibonacci number generator.  The bit of
intuition that allows us to do this is that in order to compute e.g. <img src="svgs/5f1b67e2d760d039284fdbadb2b9b9b0.svg" align=middle width=21.324435pt height=26.76201pt/>, we don't need to multiply 2 by itself 16 times.  We can rely on the fact
that <img src="svgs/6ebf32d917608acc735c2256ecd8d31c.svg" align=middle width=86.30127pt height=26.76201pt/>.
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
