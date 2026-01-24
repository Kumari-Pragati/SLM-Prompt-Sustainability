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

    def test_tree_with_one_node(self):
        root = Node(1)
        self.assertTrue(is_tree_balanced(root))

    def test_tree_with_two_nodes(self):
        root = Node(1)
        root.left = Node(2)
        self.assertTrue(is_tree_balanced(root))

    def test_tree_with_three_nodes(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        self.assertTrue(is_tree_balanced(root))

    def test_tree_with_four_nodes(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        self.assertTrue(is_tree_balanced(root))

    def test_tree_with_five_nodes(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.right.right = Node(5)
        self.assertTrue(is_tree_balanced(root))

    def test_tree_with_unbalanced_left(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.left.left = Node(4)
        self.assertFalse(is_tree_balanced(root))

    def test_tree_with_unbalanced_right(self):
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)
        root.right.right.right = Node(4)
        self.assertFalse(is_tree_balanced(root))
