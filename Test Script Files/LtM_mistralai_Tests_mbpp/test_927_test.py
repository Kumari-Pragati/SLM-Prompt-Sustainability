import unittest
from mbpp_927_code import max_height

class TestMaxHeight(unittest.TestCase):

    def test_empty_tree(self):
        self.assertEqual(max_height(None), 0)

    def test_single_node_tree(self):
        node = Node(1)
        self.assertEqual(max_height(node), 1)

    def test_two_nodes_tree(self):
        left_node = Node(1)
        right_node = Node(2)
        node = Node(3)
        node.left = left_node
        node.right = right_node
        self.assertEqual(max_height(node), 2)

    def test_balanced_tree(self):
        left_node_1 = Node(1)
        left_node_2 = Node(2)
        left_node_3 = Node(3)
        left_node_4 = Node(4)
        left_node_1.left = left_node_2
        left_node_1.right = left_node_3
        left_node_3.left = left_node_4
        right_node_1 = Node(5)
        right_node_2 = Node(6)
        node = Node(4)
        node.left = left_node_1
        node.right = right_node_1
        self.assertEqual(max_height(node), 3)

    def test_unbalanced_tree(self):
        left_node_1 = Node(1)
        left_node_2 = Node(2)
        left_node_3 = Node(3)
        left_node_4 = Node(4)
        left_node_5 = Node(5)
        left_node_6 = Node(6)
        left_node_1.left = left_node_2
        left_node_1.right = left_node_3
        left_node_3.left = left_node_4
        left_node_3.right = left_node_5
        left_node_5.left = left_node_6
        right_node_1 = Node(7)
        node = Node(4)
        node.left = left_node_1
        node.right = right_node_1
        self.assertEqual(max_height(node), 4)
