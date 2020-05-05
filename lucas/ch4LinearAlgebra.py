#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" VECTORS: abstractly, vectors are objects that can be added together (to form
new vectors) and that can be multiplied by scalars, also to form new vectors.

Concretely, vectors are points in some finite-dimensional space. They are a
good way to represent numeric data.

Ex: heights, weights and ages of a large number of people. You can treat your
data as three-dimensional vectors (height, weight, age).

The simples from-scratch approach is to represent vectors as lists of numbers.
A list of three numbers corresponds to a vector in three-dimensional space. """

height_weight_age = [70,    # inches
                     170,   # pounts
                     40 ]    # years

grades = [95,   # exam
          80,
          75,
          62 ]

# One problem with this approach is that we will want to perform arithmetic on
# vectors. Because Python lists aren't vectors, it's necessary to build these
# arithmetic tools (NumPy).

# Using lists as vectors is great for exposition but terrible for performance.
# In production code, you would want to use the NumPy library, which includes
# a high-performance array class with all sorts of arithmetic operations 
# included.

def vector_add(v, w):
    """adds corresponding elements"""
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]
    
def vector_subtract(v, w):
    """subtracts corresponding elements"""
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]
    
def vector_sum(vectors):
    """sums all corresponding elements"""
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

def vector_sum(vectors):
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the
    ith elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

import math

def magnitude(v):
    return math.sqrt(sum_of_squares(v)) # math.sqrt is square root function
    
def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return math.sqrt(squared_distance(v, w))

def distance(v, w):
    return magnitude(vector_subtract(v, w))


""" MATRICES: a matrix is a two-dimensional collection of numbers ('list of 
lists) """

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_i[j]
            for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix
    whose (i,j)th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j) # given i, create a list
             for j in range(num_cols)] # [entry_fn(i, 0), ... ]
            for i in range(num_rows)] # create one list for each i

def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return 1 if i == j else 0

























