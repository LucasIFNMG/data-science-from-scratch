#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" DESCRIBING A SINGLE SET OF DATA """
# friend counts into a histogram using Counter and plt.bar()
num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


from matplotlib import pyplot as plt
from collections import Counter

friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

# Some statistics:
num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)
sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]

# But we're only getting started!

""" CENTRAL TENDENCIES : to get some notion of where our data is centered.
Most commonly we'll use the mean(or average) or the median. """
def mean(x):
    return sum(x) / len(x)

mean(num_friends)

def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    
    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2
    
median(num_friends)
    
# The mean is very sensitive to outliers in our data
# A generalization of the median is the quantile, which represents the value
# less than which a certain percentile of the data lies
# (The median represents the value less than which 50% of the data lies).

def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

num_friends_sorted = sorted(num_friends)

quantile(num_friends, 0.10)
quantile(num_friends, 0.25)
quantile(num_friends, 0.75)
quantile(num_friends, 0.90)

# Mode: most-common value[s]:
def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]
    
mode(num_friends)
    

""" DISPERSION: referes to measures of how spread out our data is. Typically
they're statistics for which values near zero signify NOT SPREAD OUT at all and
for which large values signify VERY SPREAD out. """

# range: is the difference between the largest and smallest elements:
def data_range(x):
    return max(x) - min(x)

data_range(num_friends)

""" Like the median, the range doesn't really depend on the whole data set. A 
data set whose points are all either 0 or 100 has the same range as a data set
whose values are 0, 100, and lots of 50s.

A more complex measure of dispersion is the VARIANCE: """
def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

from ch4LinearAlgebra import sum_of_squares

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

variance(num_friends)

""" Now, whatever units our data is in (e.g., "friends"), all of our measures
of central tendency are in that same unit. Same for the range. The VARIANCE,
on the other hand, has units that are the Square of the original units ("friends
squared"). As it can be hard to make sense of there, we often look instead at
the STANDARD DEVIATION: """
import math

def standard_deviation(x):
    return math.sqrt(variance(x))

standard_deviation(num_friends)
    
# In order to avoid the outlier problem that we saw earlier for the mean, we'll
# use another alternative: INTERQUARTILE difference,  i.e, the difference
# between the 75th percentile value and the 25th percentile value:

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

interquartile_range(num_friends)

# which is quite plainly unaffected by a small number of outliers

daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]

""" CORRELATION : useful to investigate the relationship between two metrics.
e.g: amount of time people spend on a social network and their number of friends
there.

We'll first look at COVARIANCE, the paired analogue of variance.
Whereas variance measures how a single variable deviates from its mean,
Covariance measures how two variables vary in tandem('duplamente') from their means
"""
from ch4LinearAlgebra import dot

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)
    
covariance(num_friends, daily_minutes)

""" Recall that dot sums up the products of corresponding pair os elements.
When corresponding elements of x and y are either BOTH above their means or
BOTH below their means, a POSITIVE number enters the sum. 

When one is above its mean and the other below, a NEGATIVE number enters the sum.

Accordingly, a "large" positive covariance means that x tends to be large when y
is large and small when y is small.

A "large" negative covariance means the opposite: that x tends to be small when
y is large and vice versa. A covariance close to zero means that no such 
relationship exists.

CORRELATION : divides out the standard deviations of both variables: """
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0    # if no variation, correlation is zero
    
correlation(num_friends, daily_minutes) # 0.25

# The CORRELATION is unitless and always lies between -1 (perfect anti-correlation)
# and 1 (perfect correlation). A number like 0.25 represents a relatively weak
# positive correlation.

plt.scatter(num_friends, daily_minutes, s=15, c='blue', alpha=1.0)

plt.axis([0, 105, 0, 100])

plt.title("Correlation with an Outlier")
plt.xlabel("# of friends")
plt.ylabel("minutes per day")

plt.show()

# The person with 100 friends is a huge outlier. Let's ignore it:
outlier = num_friends.index(100)   # index of outlider

num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]

daily_minutes_good = [x
                      for i, x in enumerate(daily_minutes)
                      if i != outlier]

correlation(num_friends_good, daily_minutes_good)

plt.scatter(num_friends_good, daily_minutes_good, s=30, c='blue', alpha=1.0)
plt.axis([0, 50, 0, 100])
plt.title("Correlation After Removing the Outlier")
plt.xlabel("# of friends")
plt.ylabel("minutes per day")
plt.show()           
    
    
""" SIMPSON'S PARADOX : one not uncommon surprise in Data Science is when analyzing data
which correlations can be misleading when CONFOUNDING variables are ignored.

A CONFOUNDER (also confounding variable, confounding factor, or lurking variable) 
is a variable that influences both the dependent variable and independent variable, 
causing a spurious (not being what it purports to be; false; fake) association.
Confounding is a causal concept, and as such, cannot be described in terms of 
correlations or associations.    
    
For example, imagine that West Coast members has a greater avg of friends than
East coast persons. We CAN'T assume crazy theories why is that like: maybe it's
the sun, or the coffee, or the organic produce...

The key issue is that correlation is measuring the relationship between your two
variables ALL ELSE BEING EQUAL (coeteris paribus). If your data classes are
assigned at RANDOM, as they might be in a well-designed experiment, "all else
being equal" might not be a terrible assumption. But when there is a deeper 
pattern to class assignments, "all else being equal" can be an awful assumption.

The only real way to AVOID this is by KNOWING YOUR DATA and by doing what you can
to make sure you've checked for possible confounding factors. """


""" CORRELATION AND CAUSATION : 'correlation is not causation'. If x and y are
strongly correlated, that might mean that x causes y, that y causes x, that each
causes  the other, that some third factor causes both, or it might mean NOTHING. """
    