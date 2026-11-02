
# Linear Search
def linear_search(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

# Binary Search
def binary_search(a, key):
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == key:
            return mid
        elif key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

# Main Program
a = [10, 20, 30, 40, 50]
key = 30

print("Linear Search:", linear_search(a, key))
print("Binary Search:", binary_search(a, key))
