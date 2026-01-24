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

    def test_edge_case_single_node(self):
        root = Node(1)
        self.assertTrue(is_tree_balanced(root))

    def test_edge_case_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))

    def test_edge_case_left_heavy_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        self.assertFalse(is_tree_balanced(root))

    def test_edge_case_right_heavy_tree(self):
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)
        self.assertFalse(is_tree_balanced(root))

    def test_corner_case_full_binary_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.left.left.left = Node(8)
        root.left.left.right = Node(9)
        self.assertTrue(is_tree_balanced(root))
