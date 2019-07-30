import timeit
import matplotlib.pyplot as plt


# times = [
#     (
#         timeit.timeit(
#         'fib(%d)' % i,
#         setup='from fib_log import fib',
#         number=100),
#      timeit.timeit(
#          'fib(%d)' % i,
#          setup='from fib_lin import fib',
#          number=10),
#      timeit.timeit(
#          'fib(%d)' % i,
#          setup='from fib_triv import fib',
#          number=10)
#     )
#     for i in xrange(20)]
# 
# plt.plot(times, alpha=.8)
# plt.axes().get_yaxis().set_visible(False)
# plt.xlabel('n')
# plt.legend(['fib_log', 'fib_linear', 'fib_trivial'])
# plt.savefig('plot.png')
# print 'done'

import fib_log
print len(str(fib_log.fib(10000)))
