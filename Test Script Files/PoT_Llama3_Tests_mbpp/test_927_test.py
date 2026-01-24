import unittest
from mbpp_927_code import max_height

class TestMaxHeight(unittest.TestCase):

    def test_empty_tree(self):
        self.assertEqual(max_height(None), 0)

    def test_single_node_tree(self):
        node = Node(1)
        self.assertEqual(max_height(node), 1)

    def test_left_height_greater(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        self.assertEqual(max_height(node), 2)

    def test_right_height_greater(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        node.right.left = Node(4)
        self.assertEqual(max_height(node), 3)

    def test_balanced_tree(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        node.left.left = Node(4)
        node.right.right = Node(5)
        self.assertEqual(max_height(node), 3)
