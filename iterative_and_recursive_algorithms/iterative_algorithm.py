from typing import List

def dot_product(array: List[int]) -> int:
    '''
        Multiplies all non-zero elements of the given array
        iterative version
    '''
    def _contains_only_zeros(array: List[int]) -> int:
        return all([element == 0 for element in array])

    if not array:
        raise Exception("Array is empty")
    elif _contains_only_zeros(array):
        return array[0]

    # algorithm
    product = 1
    for element in array:
        if element != 0:
            product *= element
    return product

if __name__ == "__main__":
    array = [1, 2, 0, 5, 10, 0]
    print(dot_product(array))

# output: 100