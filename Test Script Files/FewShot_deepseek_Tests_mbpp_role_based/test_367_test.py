import unittest
from mbpp_367_code import is_tree_balanced

class TestIsTreeBalanced(unittest.TestCase):
    def test_typical_case(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertTrue(is_tree_balanced(root))

    def test_unbalanced_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.right.right.right = Node(8)
        self.assertFalse(is_tree_balanced(root))

    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))

    def test_single_node_tree(self):
        root = Node(1)
        self.assertTrue(is_tree_balanced(root))

    def test_two_nodes_tree(self):
        root = Node(1)
        root.left = Node(2)
        self.assertTrue(is_tree_balanced(root))

    def test_three_nodes_unbalanced_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.right.right = Node(4)
        self.assertFalse(is_tree_balanced(root))
