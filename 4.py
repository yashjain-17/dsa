
# Selection Sort
def selection_sort(a):
    for i in range(len(a)):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a

# Bubble Sort
def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# Main Program
salary = [25000.5, 40000.0, 15000.0, 50000.0, 30000.0, 60000.0]

print("Original Salaries:", salary)

s1 = selection_sort(salary.copy())
print("Selection Sort:", s1)

s2 = bubble_sort(salary.copy())
print("Bubble Sort:", s2)

print("Top 5 Highest Salaries:", s2[-5:][::-1])
