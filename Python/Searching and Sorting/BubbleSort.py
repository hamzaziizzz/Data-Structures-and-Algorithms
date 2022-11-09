def bubble_sort(input_array):
    n = len(input_array)
    for i in range(1, n):
        for j in range(0, n - i):
            if input_array[j] > input_array[j + 1]:
                temp = input_array[j]
                input_array[j] = input_array[j + 1]
                input_array[j + 1] = temp

    return input_array


print(bubble_sort([8, 3, 1, 7, 0]))
print(bubble_sort([0, 35, 676, 89, 1, 3, 6769, 0, 10, 465, 29, 4540, 65723, 655, 74, 3]))
print(bubble_sort([8, 3, 1, 7, 0, 10, 2]))
