"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    Add two arrays element-wise.

    Parameters
    ----------
    a : array_like
        Input array.
    b : array_like
        Input array.

    Returns
    -------
    c : ndarray
        The sum of `a` and `b`, element-wise.

    Examples
    --------
    >>> add([1, 2], [3, 4])
    array([4, 6])
    """
    c = np.add(x, y)
    return c

def simple_sub(a,b):
    """
    Subtract two arrays element-wise.

    Parameters
    ----------
    a : array_like
        Input array.
    b : array_like
        Input array.

    Returns
    -------
    c : ndarray
        The difference of `a` and `b`, element-wise.

    Examples
    --------
    >>> subtract([3, 4], [1, 2])
    array([2, 2])
    """
    c = np.subtract(x, y)
    return c

def simple_mult(a,b):
    """
    Multiply two arrays element-wise.

    Parameters
    ----------
    a : array_like
        Input array.
    b : array_like
        Input array.

    Returns
    -------
    c : ndarray
        The product of `a` and `b`, element-wise.

    Examples
    --------
    >>> multiply([2, 3], [4, 5])
    array([ 8, 15])
    """
    c = np.multiply(x, y)
    return c

def simple_div(a,b):
    """
    Divide two arrays element-wise.

    Parameters
    ----------
    a : array_like
        Input array.
    b : array_like
        Input array.

    Returns
    -------
    c : ndarray
        The quotient of `a` and `b`, element-wise.

    Examples
    --------
    >>> divide([10, 20], [2, 5])
    array([5., 4.])
    """
    c = np.divide(x, y)
    return c

def poly_first(x, a0, a1):
    """
    Evaluate a first-degree polynomial at the given x-values.

    The polynomial has the form a0 + a1*x, where a0 and a1 are the intercept and
    slope, respectively.

    Parameters
    ----------
    x : array_like
        The x-values at which to evaluate the polynomial.
    a0 : float
        The y-intercept of the polynomial.
    a1 : float
        The slope of the polynomial.

    Returns
    -------
    y : ndarray
        The y-values of the polynomial evaluated at the given x-values.

    Examples
    --------
    >>> poly_first([0, 1, 2], 1, 2)
    array([1, 3, 5])

    This example evaluates the polynomial y = 1 + 2*x at x = 0, 1, and 2, and
    returns the corresponding y-values [1, 3, 5].
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    Evaluate a second-degree polynomial at the given x-values.

    The polynomial has the form a0 + a1*x + a2*x^2, where a0, a1, and a2 are
    the intercept, slope, and curvature, respectively.

    Parameters
    ----------
    x : array_like
        The x-values at which to evaluate the polynomial.
    a0 : float
        The y-intercept of the polynomial.
    a1 : float
        The slope of the polynomial.
    a2 : float
        The curvature of the polynomial.

    Returns
    -------
    y : ndarray
        The y-values of the polynomial evaluated at the given x-values.

    Examples
    --------
    >>> poly_second([0, 1, 2], 1, 2, 3)
    array([ 1,  6, 15])

    This example evaluates the polynomial y = 1 + 2*x + 3*x^2 at x = 0, 1, and 2,
    and returns the corresponding y-values [1, 6, 15]. Note that this polynomial
    has a quadratic shape with positive curvature (i.e., it opens upwards).
    """
    return poly_first(x, a0, a1) + a2*(x**2)

