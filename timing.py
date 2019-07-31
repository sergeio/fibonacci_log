import timeit
import matplotlib.pyplot as plt


times = [
    (
        timeit.timeit(
        'fib(%d)' % i,
        setup='from fib_log import fib',
        number=100),
     timeit.timeit(
         'fib(%d)' % i,
         setup='from fib_lin import fib',
         number=100)
    )
    for i in xrange(10000)]

plt.plot(times, alpha=.8)
plt.axes().get_yaxis().set_visible(False)
plt.xlabel('n')
plt.legend(['fib_log', 'fib_linear'])
plt.title('Time to generate nth Fibonacci number', fontsize=10)
plt.savefig('plot.png')
print 'done'
