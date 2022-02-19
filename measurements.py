from cmath import sqrt
from locale import normalize
from pyclbr import Function
from typing import List
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

from searching_algorithms.binary_search import BinarySearch
from searching_algorithms.exponential_search import ExponentialSearch
from searching_algorithms.interpolation_search import InterpolationSearch
from searching_algorithms.searching_algorithm import SearchingAlgorithm
from sorting_algorithms.insertion_sort import InsertionSort
from timer import Timer

sns.set()
sns.set_theme()
np.random.seed(42)

class BernoulliTrial:
    def __init__(self, algorithms: List[SearchingAlgorithm], array: list):
        self.algorithms = algorithms
        self.array = array

    def perform_experiment(self, searching_value: int) -> bool:
        """
            Returns True if first algorithm is faster then second.
        """
        def _measure_algorithm_time(algorithm: SearchingAlgorithm, array: list, value: int) -> float:
            timer = Timer()
            timer.start_measuring()
            algorithm(array, value).get_result()
            return timer.stop_measuring()
        time_1, time_2 = _measure_algorithm_time(self.algorithms[0], self.array, searching_value), _measure_algorithm_time(self.algorithms[1], self.array, searching_value)
        return time_1 < time_2

def binomial_distribution(bernoulli_trial: BernoulliTrial, trials_number: int, size: int) -> list:
    experiment_results = []
    for _ in range(size):
        for searching_value in np.random.randint(0, 10**6, size=trials_number):
            experiment_results.append(bernoulli_trial.perform_experiment(searching_value))
    return experiment_results

if __name__ == "__main__":
    bernoulli_trial = BernoulliTrial(algorithms=[BinarySearch, ExponentialSearch], array=list(range(10**6)))
    print(binomial_distribution(bernoulli_trial=bernoulli_trial, trials_number=10**3, size=10**3))

