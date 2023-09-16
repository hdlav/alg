class RedBlackNode:
    def __init__(self, key, color, left=None, right=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right

class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = RedBlackNode(None, 'black')
        self.root = self.NIL_LEAF

    def left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left

        if right_child.left != self.NIL_LEAF:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right

        if left_child.right != self.NIL_LEAF:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child

    def insert(self, key):
        new_node = RedBlackNode(key, 'red')
        parent = None
        current = self.root

        while current != self.NIL_LEAF:
            parent = current

            if key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = 'black'
            return

        if new_node.parent.parent is None:
            return

        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)

                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left

                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)

                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)

        self.root.color = 'black'

    def inorder_traversal(self, node):
        if node != self.NIL_LEAF:
            self.inorder_traversal(node.left)
            print(node.key, node.color)
            self.inorder_traversal(node.right)


if __name__ == "__main__":
    rb_tree = RedBlackTree()
    keys = [10, 5, 15, 3, 7, 12, 18, 1, 6, 8, 11, 17, 20]
    for key in keys:
        rb_tree.insert(key)

    rb_tree.inorder_traversal(rb_tree.root)

