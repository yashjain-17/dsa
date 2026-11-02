
# Create hash table
table = [[] for i in range(10)]

# Hash function
def hash_function(key):
    return key % 10

# Insert function
def insert(key, value):
    index = hash_function(key)
    table[index].append([key, value])
    print("Inserted Successfully")

# Search function
def search(key):
    index = hash_function(key)

    for i in table[index]:
        if i[0] == key:
            print("Value:", i[1])
            return

    print("Key Not Found")

# Delete function
def delete(key):
    index = hash_function(key)

    for i in table[index]:
        if i[0] == key:
            table[index].remove(i)
            print("Deleted Successfully")
            return

    print("Key Not Found")

# Display function
def display():
    for i in range(10):
        print(i, ":", table[i])

# Main Program
insert(10, "Amit")
insert(20, "Rahul")
insert(15, "Neha")

print("\nHash Table:")
display()

print("\nSearch:")
search(20)

print("\nDelete:")
delete(10)

print("\nAfter Deletion:")
display()
