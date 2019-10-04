#!/usr/bin/python3
"""
101-lazy_matrix_mul module
Matrix multiplication using NumPy!
"""


import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Lazy_Matrix_Mul:
    function that uses numpy to multiply a matrix
    """
    retval = numpy.dot(m_a, m_b)
    return retval
