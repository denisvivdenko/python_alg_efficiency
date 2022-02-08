from cmath import sqrt
from typing import List
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

from searching_algorithms.binary_search import BinarySearch
from searching_algorithms.exponential_search import ExponentialSearch
from searching_algorithms.interpolation_search import InterpolationSearch
from sorting_algorithms.insertion_sort import InsertionSort
from timer import Timer

sns.set()
sns.set_theme()
np.random.seed(42)
sizes = [10, 10**2, 10**3]
measurements = {key: [] for key in sizes}
algorithms = [BinarySearch, ExponentialSearch, InterpolationSearch]
timer = Timer()

array = np.sort(np.random.randint(0, 10**9, size=10**6))

def ecdf(array):
    x = np.sort(array)
    y = np.arange(1, len(array) + 1) / len(array)
    _ = plt.plot(x, y, marker=".", linestyle="none")


def bernoulli_trial(array: List[int], size: int = 10, slice: int = 10) -> List[int]:
    first_algorithm = []
    second_algorithm = []
    searching_elements = [np.random.choice(array[:slice]) for _ in range(size)]
    for element in searching_elements:
        timer.start_measuring()
        BinarySearch(array, element).get_result()
        first_algorithm.append(timer.stop_measuring())
        timer.start_measuring()
        ExponentialSearch(array, element).get_result()
        second_algorithm.append(timer.stop_measuring())

    return [np.array(first_algorithm), np.array(second_algorithm)]

compare = lambda x: np.sum(x[0] > x[1])
# compare2 = lambda x: np.sum(x[0] < x[1])

# binomial_distribution = np.array([compare(bernoulli_trial(array, size=1000, slice=len(array))) for _ in range(1000)])
binomial_distribution2 = np.array([compare(bernoulli_trial(array, size=1000, slice=1000)) for _ in range(1000)])

# records = bernoulli_trial(array, size=100)

# print(records[0])
# # _ = plt.hist(records[0], bins=10)
# _ = plt.hist(records[1])
# plt.show()
# , density=True, stacked=True

# _ = sns.kdeplot(binomial_distribution)
_ = sns.kdeplot(binomial_distribution2)
_ = plt.xlabel("number of successes")
_ = plt.ylabel("probability")
print(f"{np.sum(binomial_distribution2 > 990) / len(binomial_distribution2)}")
plt.show()


# ecdf(binomial_distribution)
# ecdf(binomial_distribution2)


# for size in tqdm(sizes):
#     print(f"### SIZE: {size}")
#     array = np.random.randint(0, 100, size=size)
#     searching_value = np.random.choice(array)
#     sorted_array = InsertionSort(array).get_result()   
#     for algorithm in algorithms: 
#         timer.start_measuring()
#         algorithm(sorted_array, searching_value)
#         print(f"{timer.stop_measuring()%60:f}s")


