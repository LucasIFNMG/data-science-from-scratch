#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" PROBABILITY : a way of quantifying the uncertainty associated with events
chosen from a some universe of events. The universe consists of all possible
outcomes. And any subset of these outcomes is an event; Example: "the die rolls
a one".

Let's say that two events E and F are dependent if knowing something about whether
E happens gives us information about whether F happens (and vice versa). 
Otherwise they are INDEPENDENT.

E and F are independent if the probability that they both happen is the product
of the probabilities that each one happens:
    
P(E, F) = P(E)P(F)

If they are not necessarily independent (and if the probability of F is not zero), then
we define the probability of E “conditional on F” as:

P (E|F) = P(E, F) / P(F)

You should think of this as the probability that E happens, given that we know that F
happens.

We often rewrite this as:
    
P(E, F) = P(E|F)P(F)

When E and F are independent, you can check that this gives:
    
P(E|F) = P(E)

which is the mathematical way of expressing that knowing F occurred gives us no
additional information about whether E occurred.

One common tricky example involves a family with two (unknown) children.
If we assume that:
    
1. Each child is equally likely to be a boy or a girl
2. The gender of the second child is independent of the gender of the first child
then the event “no girls” has probability 1/4, the event “one girl, one boy” has proba‐
bility 1/2, and the event “two girls” has probability 1/4.

Now we can ask what is the probability of the event “both children are girls” (B) con‐
ditional on the event “the older child is a girl” (G)? Using the definition of conditional
probability:
    
P(B|G) = P(B, G) / P(G) = P(B) / P(G) = 1/2

since the event B and G (“both children are girls and the older child is a girl”) is just
the event B. (Once you know that both children are girls, it’s necessarily true that the
older child is a girl.)

Most likely this result accords with your intuition.
We could also ask about the probability of the event “both children are girls” condi‐
tional on the event “at least one of the children is a girl” (L). Surprisingly, the answer
is different from before!

As before, the event B and L (“both children are girls and at least one of the children
is a girl”) is just the event B. This means we have:
    
P(B|L) = P(B, L) / P(L) = P(B) / P(L) = 1/3

How can this be the case? Well, if all you know is that at least one of the children is a
girl, then it is twice as likely that the family has one boy and one girl than that it has
both girls.

We can check this by “generating” a lot of families: """

import random

def random_kid():
    return random.choice(["boy", "girl"])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1
        
        
print("P(both | older ): ", both_girls / older_girl)    # 0.514 ~ 1/2
print("P(both | either): ", both_girls / either_girl)   # 0.331 ~ 1/3


""" BAYES'S THEOREM : is a way of "reversing" conditional probabilities. 
To study! """

""" CONTINUOUS DISTRIBUTIONS : A coin flip corresponds to a discrete distribution,
one that associates positive probability with discrete outcomes.

Often we'll want to model distributions across a continuum of outcomes. For example,
the uniform distribution puts EQUAL WEIGHT on all the numbers between 0 and 1.

Because there are infinitely many numbers between 0 and 1, this means that the
weight it assigns to individual points must necessarily be ZERO.

For this reason, we represent a continuous distribution with a Probability
Density Function (PDF) such that the probability of seeing a value in a certain
interval equals the integral of the density function over the interval.

(If your integral calculus is rusty, a simpler way of understanding
this is that if a distribution has density function f , then the proba‐
bility of seeing a value between x and x + h is approximately
h * f x if h is small.)

The density function for the uniform distribution is just: """

def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0

# Python's random.random() is a [pseudo]random variable with a uniform density.
    
""" We will often be more interested in the Cumulative Distribution Function (cdf),
which gives the probabilty that a random variable is <= to a certain value: """

def uniform_cdf(x):
    "returns the probability that a uniform random variable is <= x"
    if x < 0: return 0  # uniform random is never less than 0
    elif x< 1: return x     # e.g. P(X <= 0.4) = 0.4
    else: return 1      # uniform random is always less than 1


""" THE NORMAL DISTRIBUTION : it is the classic bell curve-shaped distribution
and is completely determined by two parameters: its mean μ(mu) and its standard
deviation σ (sigma). The mean indicates WHERE the bell is centered, and the
standard deviation how "wide" it is: """

import math
def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

# Plot
import matplotlib.pyplot as plt

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x,sigma=1) for x in xs], '-', label='mu=0, sigma=1')
plt.plot(xs, [normal_pdf(x,sigma=2) for x in xs], '--', label='mu=0, sigma=2')
plt.plot(xs, [normal_pdf(x,sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
plt.plot(xs, [normal_pdf(x,mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
plt.legend()
plt.title("Various Normal pdfs")
plt.show()

# Cumulative Distribution Function using Python's math.erf:
def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs,[normal_cdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
plt.plot(xs,[normal_cdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
plt.plot(xs,[normal_cdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
plt.plot(xs,[normal_cdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')
plt.axis([-6, 6, 0.0, 1.0])
plt.legend(loc=4)   # bottom right
plt.title("Vairous Normal cdfs")
plt.show()

""" TO-STUDY: The Central Limit Theorem, Binomial random variables (n, p)
Introduction to Probability: http://bit.ly/1L2MTYI
                




































