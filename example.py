from math import factorial
import time
import os
import math
import urllib3
from time import sleep


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