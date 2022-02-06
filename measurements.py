import pandas as pd
import numpy as np
from tqdm import tqdm

from searching_algorithms.binary_search import BinarySearch
from searching_algorithms.exponential_search import ExponentialSearch
from searching_algorithms.interpolation_search import InterpolationSearch
from sorting_algorithms.insertion_sort import InsertionSort
from timer import Timer

np.random.seed(42)
sizes = [10, 10**2, 10**3]
measurements = {key: [] for key in sizes}
algorithms = [BinarySearch, ExponentialSearch, InterpolationSearch]
timer = Timer()

for size in tqdm(sizes):
    print(f"### SIZE: {size}")
    array = np.random.randint(0, 100, size=size)
    searching_value = np.random.choice(array)
    sorted_array = InsertionSort(array).get_result()   
    for algorithm in algorithms: 
        timer.start_measuring()
        algorithm(sorted_array, searching_value)
        print(f"{timer.stop_measuring()%60:f}s")


