# TASK:
# A list of numbers is sorted in ascending order. Using the algorithm
# binary search to find out if there is a specified number in the list. As a result, create
# tuple containing the required element and its index (value, index). If so
# there is no element, the value of the index should be equal to -1.

def binary_search(arr, number):
    if type(number) not in [int, float]:
        raise TypeError('Searched number must be int or float')
    if type(arr) not in [list, tuple]:
        raise TypeError('Array of numbers must have type "list" or "tuple"')
    sorted_arr = sorted(arr)
    start = 0
    end = len(sorted_arr) - 1
    found = False
    while start <= end:
        middle = round((start + end) / 2)
        if sorted_arr[middle] == number:
            return number, middle
        elif number > sorted_arr[middle]:
            start = middle + 1
        elif number < sorted_arr[middle]:
            end = middle - 1
    if not found:
        return number, -1

if __name__ == '__main__':
    print(binary_search([33, 132, 234.1, 52, 1, 48, 132], 234.1))
