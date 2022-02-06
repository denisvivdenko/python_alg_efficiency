from typing import List

from sorting_algorithms.sorting_algorithm import SortingAlgorithm

class InsertionSort(SortingAlgorithm):
    def _sort_array(self, array: List[int]) -> List[int]:
        array = array.copy()
        for i in range(1, len(array)):
            while array[i-1] > array[i] and i > 0:
                array[i], array[i-1] = array[i-1], array[i]
                i -= 1
        return array


if __name__ == "__main__":
    array = [14, 5, 10, 20, 4, 1, 102]
    sorting_algorithm = InsertionSort(array)
    print(sorting_algorithm.get_result())