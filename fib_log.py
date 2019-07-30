import itertools
import operator


def transpose(matrix):
    return zip(*matrix)


def m_mult(A, B):
    """Multiply matrix A by matrix B."""
    result_dim_x, result_dim_y = len(A), len(B[0])

    result = [[0 for _ in xrange(result_dim_y)]
              for _ in xrange(result_dim_x)]
    for i in xrange(result_dim_x):
        for j in xrange(result_dim_y):
            result[i][j] += sum(itertools.starmap(
                operator.mul, zip(A[i], transpose(B)[j])))

    return result


def transform_n(n):
    """Get matrix that represents `n` fibonacci transformations.

    Does matrix "exponentiation" logarithmically: A ^ n ~= (A ^ (n/2)) ^ 2
    note: n must be > 0
    """
    # return multiplier * base^n

    # Initialize base to the matrix that performs one fibonacci transformation
    # (it transforms eg [f1, f2] to [f2, f3])
    base = [[0, 1],
            [1, 1]]

    # Initialize multiplier to identity matrix
    multiplier = [[1, 0],
                  [0, 1]]

    while n > 1:
        if n % 2 == 1:
            multiplier = m_mult(multiplier, base)
            n -= 1
        else:
            base = m_mult(base, base)
            n /= 2

    return m_mult(base, multiplier)


def fib(n):
    fib_one = [[0], [1]]
    matrix = transform_n(n + 1)
    result = m_mult(matrix, fib_one)
    return result[0][0]
