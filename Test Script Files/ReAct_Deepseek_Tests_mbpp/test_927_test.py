import unittest
from mbpp_927_code import max_height

class TestMaxHeight(unittest.TestCase):

    def test_max_height_typical_case(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        node.left.left = Node(4)
        node.left.right = Node(5)
        node.right.left = Node(6)
        node.right.right = Node(7)
        self.assertEqual(max_height(node), 3)

    def test_max_height_edge_case(self):
        node = Node(1)
        self.assertEqual(max_height(node), 1)

    def test_max_height_none_case(self):
        self.assertEqual(max_height(None), 0)

    def test_max_height_single_node_case(self):
        node = Node(1)
        self.assertEqual(max_height(node), 1)

    def test_max_height_unbalanced_tree_case(self):
        node = Node(1)
        node.left = Node(2)
        node.left.left = Node(3)
        self.assertEqual(max_height(node), 2)
