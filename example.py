import math
import os
import time
from math import factorial
from time import sleep

import numpy as np
import urllib3

n_experiments = 10000
heads_count = np.random.binomial(5, 0.5, n_experiments)


heads, event_count = np.unique(heads_count, return_counts=True)

print(heads)
print(event_count)

event_prob = event_count / n_experiments

print(event_prob)


def n_choose_k(n, k):
    numerator = factorial(n) / (factorial(k) * factorial((n - k)))

    return numerator / (2**n)


def main():

    pass


if __name__ == "__main__":
    main()
