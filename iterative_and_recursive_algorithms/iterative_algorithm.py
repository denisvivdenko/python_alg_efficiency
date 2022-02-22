from typing import List


def dot_product(array: List[int]) -> int:
    '''
        Multiplies all non-zero elements of the given array
        iterative version
    '''
    product = 1
    for element in array:
        if element != 0:
            product *= element
    return product

if __name__ == "__main__":
    array = [1, 2, 0, 5, 10, 0]
    print(dot_product(array))

# output: 100