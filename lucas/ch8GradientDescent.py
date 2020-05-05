#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" GRADIENT DESCENT : useful for optimization problems, for example, when we
need to find the input v that produces the largest (or smallest) possible value.

The gradient (vector of partial derivatives) gives the input direction in which
the function most quickly increases.

One approach to maximizing a function is to pick a random starting point, compute
the gradient, take a small step in the direction of it (i.e, the direction that
causes the function to increase the most), and repeat with the new starting
point.

Important: if a function has a unique global minimum, this procedure is likely
to find it. If a function has multiple (local) minima, this procedure might 
"find" the wrong one of them, in which case you might re-run the procedure from
a variety of starting points. If a function has no minimum, then it's possible
the procedure might go on for ever.

Using the Gradient
It’s easy to see that the sum_of_squares function is smallest when its input v is a vec‐
tor of zeroes. But imagine we didn’t know that. Let’s use gradients to find the mini‐
mum among all three-dimensional vectors. We’ll just pick a random starting point
and then take tiny steps in the opposite direction of the gradient until we reach a
point where the gradient is very small: """
def step(v, direction, step_size):
    """move step_size in the direction from v"""
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]

def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]

# pick a random starting point
import random    
v = [random.randint(-10,10) for i in range(3)]

tolerance = 0.0000001

while True:
    gradient = sum_of_squares_gradient(v)   # comput the gradient at v
    next_v = step(v, gradient, -0.01)       # take a negative gradient step
    if distance(next_v, v) < tolerance:     # stop if we're converging
        break    
    v = next_v                              # continue if we're not
    
