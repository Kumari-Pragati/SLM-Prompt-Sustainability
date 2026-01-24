import unittest
from mbpp_367_code import is_tree_balanced

class TestIsTreeBalanced(unittest.TestCase):

    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))

    def test_single_node_tree(self):
        node = Node(1)
        self.assertTrue(is_tree_balanced(node))

    def test_balanced_tree(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        self.assertTrue(is_tree_balanced(node))

    def test_unbalanced_tree(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        node.right.left = Node(4)
        self.assertFalse(is_tree_balanced(node))

    def test_deeply_unbalanced_tree(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        node.left.left = Node(4)
        node.left.left.left = Node(5)
        self.assertFalse(is_tree_balanced(node))
