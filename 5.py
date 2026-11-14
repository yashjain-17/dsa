# Create hash table using separate chaining
table = [[] for _ in range(10)]


# Hash function (division method)
def hash_function(key):
    return key % len(table)


# Insert or update a key-value pair
def insert(key, value):
    index = hash_function(key)
    for pair in table[index]:
        if pair[0] == key:
            pair[1] = value
            print("Updated Successfully")
            return
    table[index].append([key, value])
    print("Inserted Successfully")


# Search function
def search(key):
    index = hash_function(key)
    for pair in table[index]:
        if pair[0] == key:
            print("Value:", pair[1])
            return pair[1]
    print("Key Not Found")
    return None


# Delete function
def delete(key):
    index = hash_function(key)
    for pair in table[index]:
        if pair[0] == key:
            table[index].remove(pair)
            print("Deleted Successfully")
            return True
    print("Key Not Found")
    return False


# Display function
def display():
    for index, bucket in enumerate(table):
        print(index, ":", bucket)


if __name__ == "__main__":
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
