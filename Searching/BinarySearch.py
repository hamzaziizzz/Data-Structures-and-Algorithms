def BinarySearch(array, key):
    array.sort()

    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        middle_index = (lower_bound + upper_bound) // 2

        if array[middle_index] == key:
            return middle_index
        else:
            if array[middle_index] > key:
                upper_bound = middle_index - 1
            else:
                lower_bound = middle_index + 1

    return -1


if __name__ == "__main__":
    array = input("Enter the elements of the list: ")
    array = [int(x) for x in list(array.split(' '))]

    print("\nAfter sorting the array:")
    print(sorted(array))
    print()

    key = int(input("Enter the element to be searched inseide the list: "))

    answer = BinarySearch(array, key)

    if answer == (-1):
        print("Given element is not present inside the list.")
    else:
        print(f"Given element is present at index {answer}")
