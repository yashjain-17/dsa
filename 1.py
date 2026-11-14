# Function to find average
def average(values):
    if not values:
        raise ValueError("Cannot calculate the average of an empty list.")
    return sum(values) / len(values)


# Function to find highest and lowest
def high_low(values):
    if not values:
        print("No borrowing records available.")
        return
    print("Highest:", max(values))
    print("Lowest:", min(values))


# Function to count zero borrowings
def zero(values):
    count = values.count(0)
    print("Zero Borrowings:", count)
    return count


# Function to find mode (first occurring value wins ties)
def mode(values):
    if not values:
        print("Mode: No data")
        return None
    result = max(set(values), key=lambda value: (values.count(value), -values.index(value)))
    print("Mode:", result)
    return result


if __name__ == "__main__":
    a = [2, 0, 2, 1, 0]
    print("Borrowing Records:", a)
    print("Average:", average(a))
    high_low(a)
    zero(a)
    mode(a)
