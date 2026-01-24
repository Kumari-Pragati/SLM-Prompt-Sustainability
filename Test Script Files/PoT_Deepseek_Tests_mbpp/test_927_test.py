import unittest
from mbpp_927_code import max_height

class TestMaxHeight(unittest.TestCase):

    def test_typical_case(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        node.left.left = Node(4)
        node.left.right = Node(5)
        node.right.left = Node(6)
        node.right.right = Node(7)
        self.assertEqual(max_height(node), 3)

    def test_edge_case_empty_tree(self):
        self.assertEqual(max_height(None), 0)

    def test_boundary_case_single_node(self):
        node = Node(1)
        self.assertEqual(max_height(node), 1)

    def test_corner_case_right_heavy_tree(self):
        node = Node(1)
        node.right = Node(2)
        node.right.right = Node(3)
        self.assertEqual(max_height(node), 3)

    def test_corner_case_left_heavy_tree(self):
        node = Node(1)
        node.left = Node(2)
        node.left.left = Node(3)
        self.assertEqual(max_height(node), 3)
