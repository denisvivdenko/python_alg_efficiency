from abc import ABC
from typing import List

class SortingAlgorithm(ABC):
    def __init__(self, array: List[int], ascending: bool = True) -> None:
        self.array = array
        self.ascending = ascending

    def get_result(self) -> List[int]:
        sorted_array = self._sort_array(self.array)
        if self.ascending:
            return sorted_array
        return sorted_array[::-1]

    def _sort_array(self, array: List[int]) -> List[int]:
        """
        Sorts given array in ascending order

        Params: 
            array (List[int]): array to sort

        Returns: List[int] sorted array
        """
        pass