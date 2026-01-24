import unittest
from mbpp_367_code import is_tree_balanced

class TestIsTreeBalanced(unittest.TestCase):

    def test_balanced_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        self.assertTrue(is_tree_balanced(root))

    def test_unbalanced_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.right.right = Node(4)
        self.assertFalse(is_tree_balanced(root))

    def test_single_node_tree(self):
        root = Node(1)
        self.assertTrue(is_tree_balanced(root))

    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))

    def test_tree_with_one_child(self):
        root = Node(1)
        root.left = Node(2)
        self.assertTrue(is_tree_balanced(root))

    def test_tree_with_two_children(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        self.assertTrue(is_tree_balanced(root))

    def test_tree_with_height_difference(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.right.right = Node(4)
        self.assertFalse(is_tree_balanced(root))
