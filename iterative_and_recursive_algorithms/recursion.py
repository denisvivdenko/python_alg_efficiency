from typing import List


def dot_product(array: List[int], product: int = 1, next_element_index: int = 0) -> int:
    '''
        Multiplies all non-zero elements of the given array
        recursive version
    '''

    # termination condition
    if len(array) == next_element_index:
        return product

    if array[next_element_index] == 0:
        return dot_product(array, product, next_element_index + 1)
    
    return dot_product(array, product * array[next_element_index], next_element_index + 1)

if __name__ == "__main__":
    array = [2, 0, 3, 4, 0]
    print(dot_product(array))

# output: 24