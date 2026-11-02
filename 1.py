
# Function to find average
def average(a):
    return sum(a) / len(a)

# Function to find highest and lowest
def high_low(a):
    print("Highest:", max(a))
    print("Lowest:", min(a))

# Function to count zero borrowings
def zero(a):
    count = 0
    for i in a:
        if i == 0:
            count += 1
    print("Zero Borrowings:", count)

# Function to find mode
def mode(a):
    print("Mode:", max(set(a), key=a.count))

# Main Program
a = [2, 0, 2, 1, 0]

print("Borrowing Records:", a)
print("Average:", average(a))

high_low(a)
zero(a)
mode(a)
