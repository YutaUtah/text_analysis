# import needed functionality
from collections import Counter

def plot_counter(counter, n_most_common=5):
    # subset the n_most_common items from the input counter
    top_items = counter.most_common(n_most_common)
    # plot "top_items"
    plot_counter_most_common(top_items)


def sum_counters(counters):
  # Sum the inputted counters
  return sum(counters, Counter())

