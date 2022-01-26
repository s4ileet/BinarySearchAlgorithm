# TASK:
# A list of numbers is sorted in ascending order. Using the algorithm
# binary search to find out if there is a specified number in the list. As a result, create
# tuple containing the required element and its index (value, index). If so
# there is no element, the value of the index should be equal to -1.

def binary_search(arr, number):
    # Raise errors
    if type(number) not in [int, float]:
        raise TypeError('Searched number must be int or float')
    if type(arr) not in [list, tuple]:
        raise TypeError('Array of numbers must have type "list" or "tuple"')
    # sorting the array
    sorted_arr = sorted(arr)
    # create the variable with the start of array
    start = 0
    # create the variable with the end of array
    end = len(sorted_arr) - 1
    # we will use this variable if there is no searched element
    found = False
    # create the loop with the condition of exit when the list is empty
    while start <= end:
        # Binary search algorithm
        # 1.Compare x with the middle element.
        # 2.If x matches with the middle element, we return the mid index.
        # 3.Else If x is greater than the mid element, then x can only lie in the right half subarray after
        # the mid element. So we recur for the right half.
        # 4.Else (x is smaller) recur for the left half.
        middle = round((start + end) / 2)
        if sorted_arr[middle] == number:
            return number, middle
        elif number > sorted_arr[middle]:
            start = middle + 1
        elif number < sorted_arr[middle]:
            end = middle - 1
    # Set a condition for a non-existing element
    if not found:
        return number, -1


if __name__ == '__main__':
    print(binary_search([33, 132, 234.1, 52, 1, 48, 132], 234.1))
