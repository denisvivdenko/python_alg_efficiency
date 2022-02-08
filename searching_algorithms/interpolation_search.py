from typing import List

from searching_algorithms.searching_algorithm import SearchingAlgorithm

class InterpolationSearch(SearchingAlgorithm):
    def _search_value(self, array: List[int], value: int) -> int:
        def _interpolationSearch(array: List[int], value: int,
                                    start_index: int = None, end_index: int = None):
            delta_index, delta_value = end_index - start_index, array[end_index] - array[start_index]
            predicted_position = int(start_index + (delta_index / delta_value) * (value - array[start_index]))

            if delta_index < 0 or value < array[start_index] or value > array[end_index]:
                raise Exception("Interpolation search: cannot find such element.")

            if array[predicted_position] == value:
                return predicted_position
            elif array[predicted_position] < value:
                return _interpolationSearch(array, value, start_index=predicted_position + 1, end_index=end_index)
            elif array[predicted_position] > value:
                return _interpolationSearch(array, value, start_index=start_index, end_index=predicted_position - 1)

        return _interpolationSearch(array, value, start_index=0, end_index=len(array) - 1)

    def __str__(self):
        return "interpolation_search"

if __name__ == "__main__":
    from ..timer import Timer

    array = list(range(10))
    timer = Timer()
    timer.start_measuring()
    exponential_search = InterpolationSearch(array, 6)
    result = exponential_search.get_result()
    performance = timer.stop_measuring()
    print(f"input: {array}\noutput: {result}\nperformance: {performance%60:f} seconds")