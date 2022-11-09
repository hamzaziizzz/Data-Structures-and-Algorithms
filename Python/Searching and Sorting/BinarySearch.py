def binary_search(input_array, value):
    left = 0
    right = len(input_array) - 1

    while left <= right:
        middle = (left + right) // 2
        if input_array[middle] == value:
            return middle
        elif value > input_array[middle]:
            left = middle + 1
        elif value < input_array[middle]:
            right = middle - 1

    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
