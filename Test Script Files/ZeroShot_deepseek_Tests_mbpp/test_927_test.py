import unittest
from mbpp_927_code import max_height, Node

class TestMaxHeight(unittest.TestCase):

    def test_empty_tree(self):
        self.assertEqual(max_height(None), 0)

    def test_single_node_tree(self):
        node = Node(1)
        self.assertEqual(max_height(node), 1)

    def test_two_nodes_tree(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.right = node2
        self.assertEqual(max_height(node1), 2)

    def test_complex_tree(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node1.left = node2
        node1.right = node3
        node2.left = node4
        node3.right = node5
        self.assertEqual(max_height(node1), 3)
