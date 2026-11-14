# Selection Sort
def selection_sort(values):
    result = values.copy()
    for i in range(len(result) - 1):
        min_index = i
        for j in range(i + 1, len(result)):
            if result[j] < result[min_index]:
                min_index = j
        result[i], result[min_index] = result[min_index], result[i]
    return result


# Bubble Sort
def bubble_sort(values):
    result = values.copy()
    for i in range(len(result)):
        swapped = False
        for j in range(len(result) - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


if __name__ == "__main__":
    salary = [25000.5, 40000.0, 15000.0, 50000.0, 30000.0, 60000.0]
    print("Original Salaries:", salary)

    s1 = selection_sort(salary)
    print("Selection Sort:", s1)

    s2 = bubble_sort(salary)
    print("Bubble Sort:", s2)
    print("Top 5 Highest Salaries:", s2[-5:][::-1])
