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
<img src="svgs/9256c7eb9d16f28115e35ea84af763c4.svg" align=middle width=101.29779pt height=27.94572pt/>, and left-multiply it by

<img src="svgs/c8d4234922966430303df9a5acf4493f.svg" align=middle width=113.698695pt height=27.94572pt/>

then the resulting vector will be
<img src="svgs/7baac4660cb00c508f1373fa4a21548a.svg" align=middle width=105.63564pt height=27.94572pt/>.

(<img src="svgs/ee1c9fcc1452eff199fcb4bda04bc783.svg" align=middle width=35.52351pt height=22.46574pt/> is the n-1th Fibonacci number, <img src="svgs/c9c53a99901c4a67544997f70b0f01bc.svg" align=middle width=18.69681pt height=22.46574pt/> is the nth and <img src="svgs/b5fc1b39bc634786995c3b0ab5dd3809.svg" align=middle width=35.340855pt height=22.46574pt/> is the
n+1th)

So we have <img src="svgs/9f8c83087c7a5cadfe110ac5e0cf89a0.svg" align=middle width=70.27383pt height=22.83138pt/>.

And it follows that if we want to advance in the sequence by two, we can just
multiply by A twice:

<img src="svgs/0968535951df4888c71c6e84446d87c9.svg" align=middle width=159.452205pt height=22.83138pt/>

<img src="svgs/3281ad70f2f279c6ae448c8c4ede7392.svg" align=middle width=82.168845pt height=26.76201pt/>

More generally, we can say that <img src="svgs/680c4edf5d0b5620b591ca8c1751e9c4.svg" align=middle width=46.619265pt height=22.83138pt/> will advance the sequence by n.

And from here, all we need is a method that computes A^n in logarithmic time to
get a logarithmic-time Fibonacci number generator.  The bit of intuition that
allows us to do this is that in order to compute e.g. <img src="svgs/3ab642dabafb8786b9db56733d4e4902.svg" align=middle width=23.812965pt height=26.76201pt/>, we don't need
to multiply 2 by itself 16 times.  We can rely on the fact that <img src="svgs/094c372df4d46a50284164aea5f5735d.svg" align=middle width=91.621035pt height=26.76201pt/>.
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
