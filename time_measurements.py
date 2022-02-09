import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

from searching_algorithms.binary_search import BinarySearch
from searching_algorithms.exponential_search import ExponentialSearch
from searching_algorithms.interpolation_search import InterpolationSearch
from sorting_algorithms.insertion_sort import InsertionSort
from sorting_algorithms.sorting_algorithm import SortingAlgorithm
from timer import Timer

def measure_time(searching_element: int=None, experiment_name: str=None) -> None:
    array_sizes = [10, 10**3, 10**6, 10**9]
    measurements = {key: [] for key in map(lambda x: str(x) + "_elements", array_sizes)}
    algorithms = [BinarySearch, ExponentialSearch, InterpolationSearch]
    timer = Timer()
    for array_size in tqdm(array_sizes):
        # array = np.random.randint(0, 10**6, size=array_size)
        # sorted_array = InsertionSort(array).get_result()
        sorted_array = list(range(array_size))
        if not searching_element:
            searching_element = np.random.choice(sorted_array)

        for algorithm in tqdm(algorithms):
            timer.start_measuring()
            try:
                algorithm(sorted_array, searching_element).get_result()
            except Exception:
                pass
            measurements[f"{array_size}_elements"].append(f"{timer.stop_measuring()%60:f}s")
    
    return pd.DataFrame(measurements, index=map(lambda x: (experiment_name, str(x(None, None))), algorithms))

print(pd.concat([measure_time(searching_element=-1, experiment_name="without element"), measure_time(experiment_name="with element")]))