#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" LINE CHART"""
from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]  # PIB

# create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color = 'green', marker = 'o', linestyle = 'solid')

# add a title
plt.title("Nominal GDP")

# add a label to the y-axis
plt.ylabel("Billions of $")
plt.show()

""" BAR CHARTS """
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# bars are by default width 0.8, so we'll add 0.1 to the left coordinates
# so that each bar is centered
xs = [i + 0.1 for i, _ in enumerate(movies)]

# plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs, num_oscars)

plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

# label x-axis with movie names at bar centers
plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)           
plt.show()

# Bar chart for plotting histograms of bucketed numeric values
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10

""" COUNTER : turns a sequence of values into a defaultdict(int)-like object
mapping keys to counts. Useful to create histograms: """
from collections import Counter
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x for x in histogram.keys()],  
        histogram.values(),                 # gove each bar its correct height 
        8)                                  # give each bar a width of 8

plt.axis([-5, 105, 0, 5])                   # x-axis from -5 to 105,
                                            # y-axis from 0 to 5

plt.xticks([10 * i for i in range(11)])     # x-axis labels at 0, 10, ..., 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()           

# Be judicious when using plt.axis(). It is considered especially bad form for
# your y-axis not to start at 0, since this is an easy way to mislead people

mentions = [500, 505]
years = [2013, 2014]

plt.bar(years, mentions, 0.8)

plt.xticks(years)
plt.ylabel("# of times I heard someone say 'Data Science'")

# if you don't do this, matplotlib will label the x-axis 0, 1
# and then add a +2.013e3 off in the corner (bad matplotlib!)
#plt.ticklabel_format(useOffset=False)

# misleading y-axis only shows the part above 500
plt.axis([2012.5, 2014.5, 499, 506])
plt.title("Look at the 'Huge' Increase!")
plt.show()      # A chart with a misleading y-axis

# Here is the fix:
plt.axis([2012.5, 2014.5, 0, 550])

plt.bar(years, mentions, 0.8)

plt.xticks(years)

plt.title("Not so Huge anymore")
plt.show()


""" LINE CHARTS : good choice for showing trends """
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

# we can make multiple calls to plt.plot
# to show multiple series on the same chart
plt.plot(xs, variance,      'g-',   label = 'variance')     # green solid line
plt.plot(xs, bias_squared,  'r-.',  label = 'bias²')        # red dot-dashed line
plt.plot(xs, total_error,   'b:',   label = 'total error')  # blue dotted line

# because we've assigned labels to each series
# we can get a legend for free
# loc=9 means "top center"
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()


""" SCATTERPLOTS : good for visualizing the relationship between two paired
sets of data. """
# (Social Network) Number of friends vs Number of minutes they spend on the site
friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

# label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
        xy=(friend_count, minute_count),    # put the label with its point
        xytext=(5, -5),                     # but slightly offset
        textcoords='offset points')

plt.title("Daily minutes vs. Number of Friends")
                 
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()

# if you're scattering comparable variables, you might get a misleading
# picture if you let maplotlib choose the scale:
test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Aren't Comparable")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")
plt.show()

# if we include a call to plt.axis("equal"), the plot more accurately shows
# that most of the variation occurs on test 2
plt.scatter(test_1_grades, test_2_grades)

plt.axis("equal")

plt.title("Axes Are Comparable")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")
plt.show()

""" FOR FURTHER EXPLORATION : 
SEABORN: (PRETTIER AND MORE COMPLEX)
D3.js: sophisticated interactive visualizations for the web
Bokeh: lib that brings D3-style visualizations into Python
ggplot : Python port of the popular R lib ggplot2, which is widely used for
creating "publication quality" charts and graphics. """
