class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def display(root):
    if root:
        display(root.left)
        print(root.data, end=" ")
        display(root.right)


def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    if key < root.data:
        return search(root.left, key)

    return search(root.right, key)


def minimum(root):
    if root.left is None:
        return root.data
    return minimum(root.left)


def delete(root, key):
    if root is None:
        return None

    if key < root.data:
        root.left = delete(root.left, key)

    elif key > root.data:
        root.right = delete(root.right, key)

    else:
        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        root.data = minimum(root.right)
        root.right = delete(root.right, root.data)

    return root


# Main program
root = None

root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)

print("BST:")
display(root)

print("\nSearch 30:", search(root, 30))

root = delete(root, 30)

print("After Deletion:")
display(root)