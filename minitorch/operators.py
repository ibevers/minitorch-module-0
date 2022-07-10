"""
Collection of the core mathematical operators used throughout the code base.
"""

import math

# ## Task 0.1

# Implementation of a prelude of elementary functions.


def mul(x, y):
    ":math:`f(x, y) = x * y`"
    return x * y


def id(x):
    ":math:`f(x) = x`"
    return x

def add(x, y):
    ":math:`f(x, y) = x + y`"
    return x + y


def neg(x):
    ":math:`f(x) = -x`"
    return -x

def lt(x, y):
    ":math:`f(x) =` 1.0 if x is less than y else 0.0"
    if x < y:
        return 1.0 
    else:
        return 0.0

def eq(x, y):
    ":math:`f(x) =` 1.0 if x is equal to y else 0.0"
    if x == y:
        return 1.0 
    else:
        return 0.0


def max(x, y):
    ":math:`f(x) =` x if x is greater than y else y"
    if x > y:
        return x 
    else: 
        return y

def is_close(x, y):
    ":math:`f(x) = |x - y| < 1e-2` "
    return math.isclose(x, y, abs_tol=1e-2)

def sigmoid(x):
    r"""
    :math:`f(x) =  \frac{1.0}{(1.0 + e^{-x})}`

    (See `<https://en.wikipedia.org/wiki/Sigmoid_function>`_ .)

    Calculate as

    :math:`f(x) =  \frac{1.0}{(1.0 + e^{-x})}` if x >=0 else :math:`\frac{e^x}{(1.0 + e^{x})}`

    for stability.

    Args:
        x (float): input

    Returns:
        float : sigmoid value
    """
    sig = 0
    if x>= 0:
        sig = 1.0/(1.0 + math.exp(-x))
        if is_close(sig, 1):
            return 1 - 1e-10
    else:
        sig = math.exp(-x)/(1.0 + math.exp(-x))
        if is_close(sig, 1):
            return 0 + 1e-10
    return sig


def relu(x):
    """
    :math:`f(x) =` x if x is greater than 0, else 0

    (See `<https://en.wikipedia.org/wiki/Rectifier_(neural_networks)>`_ .)

    Args:
        x (float): input

    Returns:
        float : relu value
    """
    if x > 0:
        return x
    else:
        return 0

EPS = 1e-6


def log(x):
    ":math:`f(x) = log(x)`"
    return math.log(x + EPS)


def exp(x):
    ":math:`f(x) = e^{x}`"
    return math.exp(x)


def log_back(x, d):
    r"If :math:`f = log` as above, compute d :math:`d \times f'(x)`"
    return d * inv(x)

def inv(x):
    ":math:`f(x) = 1/x`"
    if x == 0:
        assert "cannot divide by zero"
    return 1/x


def inv_back(x, d):
    r"If :math:`f(x) = 1/x` compute d :math:`d \times f'(x)`"
    return d * math.pow(-x, -2)

def relu_back(x, d):
    r"If :math:`f = relu` compute d :math:`d \times f'(x)`"
    if x > 0:
        return d
    else:
        return 0

# ## Task 0.3

# Small library of elementary higher-order functions for practice.


def map(fn):
    """
    Higher-order map.

    .. image:: figs/Ops/maplist.png


    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (one-arg function): Function from one value to one value.

    Returns:
        function : A function that takes a list, applies `fn` to each element, and returns a
        new list
    """
    return lambda ls: [fn(ls[i]) for i in range(len(ls))]


def negList(ls):
    "Use :func:`map` and :func:`neg` to negate each element in `ls`"
    m = map(neg)
    return m(ls)


def zipWith(fn):
    """
    Higher-order zipwith (or map2).

    .. image:: figs/Ops/ziplist.png

    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (two-arg function): combine two values

    Returns:
        function : takes two equally sized lists `ls1` and `ls2`, produce a new list by
        applying fn(x, y) on each pair of elements.

    """
    return lambda ls1, ls2: [fn(ls1[i], ls2[i]) for i in range(len(ls1))]


def addLists(ls1, ls2):
    "Add the elements of `ls1` and `ls2` using :func:`zipWith` and :func:`add`"
    f = zipWith(add)
    return f(ls1, ls2)

def reduce(fn, start):
    r"""
    Higher-order reduce.

    .. image:: figs/Ops/reducelist.png


    Args:
        fn (two-arg function): combine two values
        start (float): start value :math:`x_0`

    Returns:
        function : function that takes a list `ls` of elements
        :math:`x_1 \ldots x_n` and computes the reduction :math:`fn(x_3, fn(x_2,
        fn(x_1, x_0)))`
    """
    return lambda ls: fn(ls[2], fn(ls[1], fn(ls[0], start)))

def sum(ls):
    "Sum up a list using :func:`reduce` and :func:`add`."
    for i in range(3 - len(ls)%3):
        ls.append(0)
    r = reduce(add, 0)
    sum = 0
    for i in range(0, len(ls), 3):
        sum += r(ls)
        for i in range(3): ls.append(ls.pop(0))
    return sum


def prod(ls):
    "Product of a list using :func:`reduce` and :func:`mul`."
    # TODO: Implement for Task 0.3 
    for i in range(3 - len(ls)%3):
        ls.append(1)
    r = reduce(mul, 1)
    prod = 1
    for i in range(0, len(ls), 3):
        prod *= r(ls)
        for i in range(3): ls.append(ls.pop(0))
    return prod
