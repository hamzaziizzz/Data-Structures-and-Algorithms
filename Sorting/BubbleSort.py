def BubbleSort(array):
    number_of_iterations = len(array) - 1

    i = 1
    while i <= number_of_iterations:
        maximum = array[0]
        for index in range(1, (len(array) - i) + 1):
            if maximum > array[index]:
                temp = array[index]
                array[index] = maximum
                array[index - 1] = temp
            elif maximum < array[index]:
                maximum = array[index]

        i = i + 1

    return array

if __name__ == "__main__":
    array = input("Enter the elements of the list: ")
    array = [int(x) for x in list(array.split(' '))]

    sorted_array = BubbleSort(array)
    print("After applying bubble sort:")
    print(sorted_array)
