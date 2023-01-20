def LinearSearch(array, key):
    for element in array:
        if element == key:
            return array.index(element)

    return -1


if __name__ == "__main__":
    array = input("Enter the elements of the list: ")
    array = list(array.split(' '))

    print()
    print(array)
    print()

    key = input("Enter the element to be searched inseide the list: ")

    answer = LinearSearch(array, key)

    if answer == (-1):
        print("Given element is not present inside the list.")
    else:
        print(f"Given element is present at index {answer}")
