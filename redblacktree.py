class RBNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'RED'


class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = RBNode(0)
        self.NIL_LEAF.color = 'BLACK'
        self.root = self.NIL_LEAF
        self.node_count = 0

    def insert(self, key):
        new_node = RBNode(key)
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF
        self._insert_bst(new_node)
        self._fix_insert(new_node)
        self.node_count += 1

    def _insert_bst(self, node):
        parent = None
        current = self.root

        while current != self.NIL_LEAF:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._rotate_left(node.parent.parent)
        self.root.color = 'BLACK'

    def delete(self, key):
        node = self.search(self.root, key)
        if node == self.NIL_LEAF:
            print(f"{key} not found in the Red-Black Tree. Deletion not performed.")
            return
        self._delete_node(node)

    def _delete_node(self, node):
        original_color = node.color
        if node.left == self.NIL_LEAF:
            temp = node.right
            self._transplant(node, node.right)
        elif node.right == self.NIL_LEAF:
            temp = node.left
            self._transplant(node, node.left)
        else:
            successor = self.min_value_node(node.right)
            original_color = successor.color
            temp = successor.right
            if successor.parent == node:
                temp.parent = successor
            else:
                self._transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self._transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor
            successor.color = node.color

        if original_color == 'BLACK':
            self._fix_delete(temp)
        self.node_count -= 1

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _fix_delete(self, node):
        while node != self.root and node.color == 'BLACK':
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    node.parent.color = 'RED'
                    self._rotate_left(node.parent)
                    sibling = node.parent.right
                if sibling.left.color == 'BLACK' and sibling.right.color == 'BLACK':
                    sibling.color = 'RED'
                    node = node.parent
                else:
                    if sibling.right.color == 'BLACK':
                        sibling.left.color = 'BLACK'
                        sibling.color = 'RED'
                        self._rotate_right(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = 'BLACK'
                    sibling.right.color = 'BLACK'
                    self._rotate_left(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    node.parent.color = 'RED'
                    self._rotate_right(node.parent)
                    sibling = node.parent.left
                if sibling.right.color == 'BLACK' and sibling.left.color == 'BLACK':
                    sibling.color = 'RED'
                    node = node.parent
                else:
                    if sibling.left.color == 'BLACK':
                        sibling.right.color = 'BLACK'
                        sibling.color = 'RED'
                        self._rotate_left(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = 'BLACK'
                    sibling.left.color = 'BLACK'
                    self._rotate_right(node.parent)
                    node = self.root
        node.color = 'BLACK'

    def search(self, node, key):
        if node == self.NIL_LEAF or node.key == key:
            return node
        if key < node.key:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def min_value_node(self, node):
        while node.left != self.NIL_LEAF:
            node = node.left
        return node

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node != self.NIL_LEAF:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

    def _rotate_left(self, node):
        y = node.right
        node.right = y.left
        if y.left != self.NIL_LEAF:
            y.left.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y
        y.color = 'BLACK'
        node.color = 'RED'

    def _rotate_right(self, node):
        y = node.left
        node.left = y.right
        if y.right != self.NIL_LEAF:
            y.right.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y
        y.color = 'BLACK'
        node.color = 'RED'

    def visualize(self):
        self._visualize(self.root, 0)

    def _visualize(self, node, level):
        if node != self.NIL_LEAF:
            self._visualize(node.right, level + 1)
            print(" " * 4 * level + f"{node.key} ({node.color})")
            self._visualize(node.left, level + 1)


def rbt_program():
    rbt = RedBlackTree()
    while True:
        print("\nRed-Black Tree Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. In-order Traversal")
        print("5. Visualize Tree Structure")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if not choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        choice = int(choice)

        if choice == 1:
            key = input("Enter value to insert: ")
            if not key.isdigit():
                print("Please enter a valid integer.")
                continue
            rbt.insert(int(key))
            print(f"{key} inserted.")
        elif choice == 2:
            key = input("Enter value to delete: ")
            if not key.isdigit():
                print("Please enter a valid integer.")
                continue
            rbt.delete(int(key))
        elif choice == 3:
            key = input("Enter value to search: ")
            if not key.isdigit():
                print("Please enter a valid integer.")
                continue
            found_node = rbt.search(rbt.root, int(key))
            if found_node != rbt.NIL_LEAF:
                print(f"{key} found in Red-Black Tree.")
            else:
                print(f"{key} not found in Red-Black Tree.")
        elif choice == 4:
            print("In-order Traversal:",
