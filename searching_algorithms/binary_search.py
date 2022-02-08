from typing import List

from searching_algorithms.searching_algorithm import SearchingAlgorithm

class BinarySearch(SearchingAlgorithm):
    def _search_value(self, array: List[int], value: int) -> int:
        def _binary_search(array: List[int], value: int, start_index: int, end_index: int) -> int:
            if start_index > end_index:
                raise Exception("Binary search: value have not been found.")
                
            middle_index = int(start_index + (end_index - start_index) / 2)
            if array[middle_index] == value:
                return middle_index
            elif array[middle_index] < value:
                return _binary_search(array, value, middle_index + 1, end_index)
            elif array[middle_index] > value:
                return _binary_search(array, value, start_index, middle_index - 1)

        return _binary_search(array, value, 0, len(array) - 1)
    
    def __str__(self):
        return "binary_search"


if __name__ == "__main__":
    from timer import Timer

    array = list(range(10))
    timer = Timer()
    timer.start_measuring()
    binary_search = BinarySearch(array, 6)
    result = binary_search.get_result()
    performance = timer.stop_measuring()
    print(f"input: {array}\noutput: {result}\nperformance: {performance%60:f} seconds")
