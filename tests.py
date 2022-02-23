'''
python -m pytest tests.py -W ignore::DeprecationWarning
'''

import pytest

from sorting_algorithms.insertion_sort import InsertionSort
from searching_algorithms.binary_search import BinarySearch
from searching_algorithms.exponential_search import ExponentialSearch
from searching_algorithms.interpolation_search import InterpolationSearch
from searching_algorithms.searching_algorithm import SearchingAlgorithm
from iterative_and_recursive_algorithms.recursion import dot_product as dot_product_iterative
from iterative_and_recursive_algorithms.iterative_algorithm import dot_product as dot_product_recursive

algorithms = [BinarySearch, ExponentialSearch, InterpolationSearch]
iter_algorithms = [dot_product_iterative, dot_product_recursive]

def test_insertion_sort_passing() -> None:
    array = [14, 5, 10, 20, 4, 1, 102]
    expected = [1, 4, 5, 10, 14, 20, 102]
    actual = InsertionSort(array).get_result()
    assert expected == actual

@pytest.mark.parametrize("searching_algorithm", algorithms)
def test_search_end_passing(searching_algorithm: SearchingAlgorithm) -> None:
    array = list(range(10))
    value = 8
    expected = 8
    actual = searching_algorithm(array, value).get_result()
    assert expected == actual

@pytest.mark.parametrize("searching_algorithm", algorithms)
def test_search_start_passing(searching_algorithm: SearchingAlgorithm) -> None:
    array = list(range(10))
    value = 2
    expected = 2
    actual = searching_algorithm(array, value).get_result()
    assert expected == actual

@pytest.mark.parametrize("searching_algorithm", algorithms)
def test_search_middle_passing(searching_algorithm: SearchingAlgorithm) -> None:
    array = list(range(10))
    value = 4
    expected = 4
    actual = searching_algorithm(array, value).get_result()
    assert expected == actual

@pytest.mark.parametrize("searching_algorithm", algorithms)
def test_search_exception(searching_algorithm: SearchingAlgorithm) -> None:
    with pytest.raises(Exception) as not_found:
        array = list(range(10))
        actual = searching_algorithm(array, 100).get_result()

def test_dot_product_recursive() -> None:
    array = [0, 2, 10, 5, 3]
    expected = 300
    actual = dot_product_recursive(array)
    assert expected == actual

def test_dot_product_iterative() -> None:
    array = [0, 2, 10, 5, 3]
    expected = 300
    actual = dot_product_iterative(array)
    assert expected == actual

@pytest.mark.parametrize("iter_algorithm", iter_algorithms)
def test_dot_product_one_zero(iter_algorithm) -> None:
    array = [0]
    expected = 0
    actual = iter_algorithm(array)
    assert expected == actual

@pytest.mark.parametrize("iter_algorithm", iter_algorithms)
def test_dot_product_zeros(iter_algorithm) -> None:
    array = [0, 0, 0]
    expected = 0
    actual = iter_algorithm(array)
    assert expected == actual

@pytest.mark.parametrize("iter_algorithm", iter_algorithms)
def test_empty_array_dot_product(iter_algorithm) -> None:
    array = []
    with pytest.raises(Exception) as not_found:
        iter_algorithm(array).get_result()
    
