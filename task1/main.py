class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1


class Tree:
    def __init__(self, root=None):
        self.root = root

    def build_by_arr(self, arr):
        if len(arr) == 0:
            return

        arr = sorted(arr)
        i = 0
        mid = len(arr) // 2
        self.root = self.insert(arr[mid], self.root)

        while i < len(arr):
            if i != mid:
                self.root = self.insert(arr[i], self.root)
            i += 1

    def get_height(self, node: Node) -> int:
        if not node:
            return 0
        return node.height

    def update_height(self, node: Node):
        if node is not None:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def count_nodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def check(self, root: Node) -> bool:
        def check_balanced(node):
            if node is None:
                return True, 0

            left_balanced, left_height = check_balanced(node.left)
            right_balanced, right_height = check_balanced(node.right)

            height = max(left_height, right_height) + 1
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

            return balanced, height

        b, h = check_balanced(root)
        return b

    def left_rotate(self, node: Node) -> Node:
        transporting_node = node.right
        if transporting_node is None:
            return node

        node.right = transporting_node.left
        transporting_node.left = node
        self.update_height(node)
        self.update_height(transporting_node)
        return transporting_node

    def right_rotate(self, node: Node) -> Node:
        transporting_node = node.left
        if transporting_node is None:
            return node

        node.left = transporting_node.right
        transporting_node.right = node
        self.update_height(node)
        self.update_height(transporting_node)
        return transporting_node

    def balance_tree(self, val, node: Node) -> Node:
        self.update_height(node)
        if self.get_height(node.left) - self.get_height(node.right) >= 2:
            if val < node.left.val:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        elif self.get_height(node.right) - self.get_height(node.left) >= 2:
            if val > node.right.val:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node

    def insert(self, val:int, node: Node) -> Node:
        if val < 0:
            raise Exception("Число должно быть натуральным")
        if node is None:
            return Node(val)
        if val <= node.val:
            node.left = self.insert(val, node.left)
        else:
            node.right = self.insert(val, node.right)

        return self.balance_tree(val, node)

    def find_min_max(self, node: Node, key) -> Node:
        cur = node
        if key:
            while cur.right:
                cur = cur.right
        else:
            while cur.left:
                cur = cur.left
        return cur

    def find_average(self, root) -> float:
        def find_sum_and_count(node):
            if node is None:
                return 0, 0

            left_sum, left_count = find_sum_and_count(node.left)
            right_sum, right_count = find_sum_and_count(node.right)

            return node.val + left_sum + right_sum, 1 + left_count + right_count

        s, c = find_sum_and_count(root)
        if c == 0:
            return 0

        return s / c

    def inorder(self, root) -> list:
        result = []

        def inorder_iteration(node):
            if node is not None:
                inorder_iteration(node.left)
                result.append(node.val)
                inorder_iteration(node.right)

        inorder_iteration(root)
        return result

    def delete_node(self, val, node: Node) -> Node:
        if node is None:
            return None

        if val < node.val:
            node.left = self.delete_node(val, node.left)
        elif val > node.val:
            node.right = self.delete_node(val, node.right)
        else:
            if node.right is None:
                return node.left
            else:
                min_right = self.find_min_max(node.right, False)
                node.val = min_right.val
                node.right = self.delete_node(min_right.val, node.right)

        return self.balance_tree(node.val, node)

    def delete_min_node(self, node: Node) -> Node:
        if not node:
            return node
        if not node.left:
            return node.right
        node.left = self.delete_min_node(node.left)
        return self.balance_tree(node.val, node)

    def delete_max_node(self, node: Node) -> Node:
        if not node:
            return node
        if not node.right:
            return node.left
        node.right = self.delete_max_node(node.right)
        return self.balance_tree(node.val, node)

    def split(self, val, root):
        if root is None:
            return None, None

        arr = self.inorder(root)
        left = []
        right = []
        i = 0
        while arr[i] <= val and i < len(arr):
            left.append(arr[i])
            i += 1

        while i < len(arr):
            right.append(arr[i])
            i += 1

        left_tree = Tree()
        left_tree.build_by_arr(left)
        right_tree = Tree()
        right_tree.build_by_arr(right)

        return left_tree, right_tree

    def print_tree(self, node: Node, level: int = 0, prefix: str = "Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.val))

            if node.left is not None or node.right is not None:
                if node.left is not None:
                    self.print_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")

                if node.right is not None:
                    self.print_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")


def merge(tree1, tree2):
    if tree1 is None and tree2 is None:
        return None

    if tree1 is None:
        return tree2

    if tree2 is None:
        return tree1

    tree2_values = tree2.inorder(tree2.root)
    for x in tree2_values:
        tree1.root = tree1.insert(x, tree1.root)

    return tree1

