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
        root.right = Node(4)
        self.assertFalse(is_tree_balanced(root))

    def test_single_node_tree(self):
        root = Node(1)
        self.assertTrue(is_tree_balanced(root))

    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))

    def test_tree_with_left_subtree(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        self.assertTrue(is_tree_balanced(root))

    def test_tree_with_right_subtree(self):
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)
        self.assertTrue(is_tree_balanced(root))

    def test_tree_with_left_and_right_subtrees(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.right.right = Node(5)
        self.assertTrue(is_tree_balanced(root))

    def test_tree_with_height_difference(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.right.right = Node(5)
        root.left.left.left = Node(6)
        self.assertFalse(is_tree_balanced(root))
