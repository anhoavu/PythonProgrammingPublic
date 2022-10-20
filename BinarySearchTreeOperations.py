from BinarySearchTreeHelper import _build_tree_string

class BSTNode:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.parent = None
        self.left = left
        self.right = right
        if left != None:
            left.parent = self
        if right != None:
            right.parent = self

    def __str__(self):
        lines = _build_tree_string(self, 0, False, "-")[0]
        return "\n" + "\n".join((line.rstrip() for line in lines))

class BST:
    def __init__(self, root):
        self.root = root

    def __str__(self):
        return str(self.root)

def search(x, key):
    # Implement using pseudocode in the book
    pass

def minimum(x):
    # Implement using pseudocode in the book
    pass

def maximum(x):
    # Implement using pseudocode in the book
    pass

def successor(x):
    # Implement using pseudocode in the book
    pass

def predecessor(x):
    # Implement using pseudocode in the book
    pass

def insert(T, z):
    # Implement using pseudocode in the book
    pass

def delete(T, z):
    # Implement using pseudocode in the book
    pass

def testBST():
    # Write the code to construct the tree in Figure 12.2
    print(root)

    # Write the code to test your implementation above

testBST()
