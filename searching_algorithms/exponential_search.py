from typing import List

from searching_algorithms.searching_algorithm import SearchingAlgorithm
from searching_algorithms.binary_search import BinarySearch

class ExponentialSearch(SearchingAlgorithm):
    def _search_value(self, array: List[int], value: int) -> int:
        if len(array) <= 0:
            raise Exception("Eponential search: cannot find value.")

        index = 1
        while index < len(array):
            if array[index] >= value:
                break
            index *= 2
        lower_bound = int(index / 2)
        return lower_bound + BinarySearch(array[lower_bound: index], value).get_result()

    def __str__(self):
        return "exponential_search"

if __name__ == "__main__":
    from ..timer import Timer

    array = list(range(10))
    timer = Timer()
    timer.start_measuring()
    exponential_search = ExponentialSearch(array, 6)
    result = exponential_search.get_result()
    performance = timer.stop_measuring()
    print(f"input: {array}\noutput: {result}\nperformance: {performance%60:f} seconds")
