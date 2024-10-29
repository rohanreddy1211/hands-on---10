class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.node_count = 0

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            self.node_count += 1
        else:
            if self._insert_recursive(self.root, key):
                self.node_count += 1
        print(f"Current node count: {self.node_count}")

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
                return True
            else:
                return self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
                return True
            else:
                return self._insert_recursive(node.right, key)

    def search(self, key):
        result = self._search_recursive(self.root, key)
        if result:
            print(f"{key} found in BST.")
        else:
            print(f"{key} not found in BST.")

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        if self.root is None:
            print(f"{key} not found in BST.")
            return
        self.root, deleted = self._delete_recursive(self.root, key)
        if deleted:
            self.node_count -= 1
            print(f"{key} deleted.")
        else:
            print(f"{key} not found in BST.")
        print(f"Current node count: {self.node_count}")

    def _delete_recursive(self, node, key):
        if node is None:
            return node, False

        if key < node.key:
            node.left, deleted = self._delete_recursive(node.left, key)
            return node, deleted
        elif key > node.key:
            node.right, deleted = self._delete_recursive(node.right, key)
            return node, deleted

        if node.left is None:
            return node.right, True
        elif node.right is None:
            return node.left, True

        temp = self._min_value_node(node.right)
        node.key = temp.key
        node.right, _ = self._delete_recursive(node.right, temp.key)
        return node, True

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        return self._inorder_recursive(self.root, [])

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)
        return result

    def depth(self):
        return self._depth_recursive(self.root)

    def _depth_recursive(self, node):
        if node is None:
            return 0
        left_depth = self._depth_recursive(node.left)
        right_depth = self._depth_recursive(node.right)
        return max(left_depth, right_depth) + 1

    def visualize(self):
        self._visualize(self.root, 0)

    def _visualize(self, node, level):
        if node is not None:
            self._visualize(node.right, level + 1)
            print(" " * 4 * level + f"{node.key}")
            self._visualize(node.left, level + 1)


def bst_program():
    bst = BinarySearchTree()
    while True:
        print("\nBinary Search Tree Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. In-order Traversal")
        print("5. Visualize Tree Structure")
        print("6. Get Tree Depth")
        print("7. Exit")
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        if choice == 1:
            key = input("Enter value to insert: ")
            try:
                key = int(key)
                bst.insert(key)
            except ValueError:
                print("Please enter a valid integer.")
        elif choice == 2:
            key = input("Enter value to delete: ")
            try:
                key = int(key)
                bst.delete(key)
            except ValueError:
                print("Please enter a valid integer.")
        elif choice == 3:
            key = input("Enter value to search: ")
            try:
                key = int(key)
                bst.search(key)
            except ValueError:
                print("Please enter a valid integer.")
        elif choice == 4:
            print("In-order Traversal:", bst.inorder())
        elif choice == 5:
            print("Tree Structure:")
            bst.visualize()
        elif choice == 6:
            print(f"The depth of the tree is: {bst.depth()}.")
        elif choice == 7:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

bst_program()
