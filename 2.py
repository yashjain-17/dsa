
# Two stacks
undo_stack = []
redo_stack = []

document = ""

# Make a change
def make_change(text):
    global document
    undo_stack.append(document)
    document = text
    redo_stack.clear()

# Undo operation
def undo():
    global document
    if undo_stack:
        redo_stack.append(document)
        document = undo_stack.pop()
    else:
        print("Nothing to undo")

# Redo operation
def redo():
    global document
    if redo_stack:
        undo_stack.append(document)
        document = redo_stack.pop()
    else:
        print("Nothing to redo")

# Display document
def display():
    print("Document:", document)


# Main program
make_change("Hello")
make_change("Hello World")
display()

undo()
print("After Undo:")
display()

redo()
print("After Redo:")
display()
