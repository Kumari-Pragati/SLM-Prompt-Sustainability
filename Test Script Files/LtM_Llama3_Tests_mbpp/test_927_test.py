import unittest
from mbpp_927_code import max_height

class TestMaxHeight(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(max_height(None), 0)

    def test_single_node_tree(self):
        node = Node(1)
        self.assertEqual(max_height(node), 1)

    def test_balanced_tree(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        self.assertEqual(max_height(node), 2)

    def test_unbalanced_tree(self):
        node = Node(1)
        node.left = Node(2)
        node.left.left = Node(3)
        self.assertEqual(max_height(node), 3)

    def test_tree_with_multiple_levels(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        node.left.left = Node(4)
        node.left.right = Node(5)
        self.assertEqual(max_height(node), 3)
