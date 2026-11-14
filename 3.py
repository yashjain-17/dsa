# Linear Search
def linear_search(values, key):
    for index, value in enumerate(values):
        if value == key:
            return index
    return -1


# Binary Search (input list must be sorted in ascending order)
def binary_search(values, key):
    low = 0
    high = len(values) - 1

    while low <= high:
        mid = (low + high) // 2

        if values[mid] == key:
            return mid
        if key < values[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


if __name__ == "__main__":
    a = [10, 20, 30, 40, 50]
    key = 30
    print("Linear Search:", linear_search(a, key))
    print("Binary Search:", binary_search(a, key))
