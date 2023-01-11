#!/usr/bin/python3
"""
Multiplying matrices with numpy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ Multiplies matrices using 'matmul' in numpy"""
    return numpy.matmul(m_a, m_b)
