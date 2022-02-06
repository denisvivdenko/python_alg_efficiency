from abc import ABC
from typing import List

class SearchingAlgorithm(ABC):
    def __init__(self, array: List[int], value: int) -> None:
        """
        Params:
            array (List[int]): array of values
            value (int): searching value
        """
        self._array = array
        self._value = value

    def get_result(self) -> int:
        """
        Returns: index of the first occurance of the value in the given array
        """
        return self._search_value(self._array, self._value)

    def _search_value(self, array: List[int], value: int) -> int:
        """
        Searches for first occurance of value in the ordered array.

        Params: 
            array (List[int]): array of digits
            value (int): searching value

        Returns: index of the value
        """
        pass