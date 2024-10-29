class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def delete(self, root, key):
        if not root:
            print(f"{key} not found in AVL Tree.")
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if not root:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.min_value_node(node.left)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def inorder(self, node, result):
        if node:
            self.inorder(node.left, result)
            result.append(node.key)
            self.inorder(node.right, result)
        return result

    def count_nodes(self, node):
        if not node:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def visualize(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))
            self.visualize(node.left, level + 1, "L--- ")
            self.visualize(node.right, level + 1, "R--- ")


def avl_program():
    avl = AVLTree()
    root = None
    while True:
        print("\nAVL Tree Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. In-order Traversal")
        print("5. Visualize Tree Structure")
        print("6. Node Count")
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
                root = avl.insert(root, key)
                print(f"{key} inserted. Current node count: {avl.count_nodes(root)}.")
            except ValueError:
                print("Please enter a valid integer.")
        elif choice == 2:
            key = input("Enter value to delete: ")
            try:
                key = int(key)
                root = avl.delete(root, key)
                print(f"{key} deleted. Current node count: {avl.count_nodes(root)}.")
            except ValueError:
                print("Please enter a valid integer.")
        elif choice == 3:
            key = input("Enter value to search: ")
            try:
                key = int(key)
                found_node = avl.search(root, key)
                if found_node:
                    print(f"{key} found in AVL Tree.")
                else:
                    print(f"{key} not found in AVL Tree.")
            except ValueError:
                print("Please enter a valid integer.")
        elif choice == 4:
            print("In-order Traversal:", avl.inorder(root, []))
        elif choice == 5:
            print("Tree Structure:")
            avl.visualize(root)
        elif choice == 6:
            print(f"Total nodes in AVL Tree: {avl.count_nodes(root)}.")
        elif choice == 7:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

avl_program()
