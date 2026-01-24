import unittest
from mbpp_367_code import is_tree_balanced

class TestIsTreeBalanced(unittest.TestCase):
    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))

    def test_single_node_tree(self):
        node = Node(1)
        self.assertTrue(is_tree_balanced(node))

    def test_unbalanced_tree(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        node_1.left = node_2
        node_1.right = node_3
        node_3.left = node_4
        node_3.right = node_5
        self.assertFalse(is_tree_balanced(node_1))

    def test_balanced_tree(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        node_6 = Node(6)
        node_1.left = node_2
        node_1.right = node_3
        node_3.left = node_4
        node_3.right = node_5
        node_5.left = node_6
        self.assertTrue(is_tree_balanced(node_1))
