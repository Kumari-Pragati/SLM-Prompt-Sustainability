import unittest
from mbpp_927_code import max_height

class TestMaxHeight(unittest.TestCase):
    def test_normal_input(self):
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

    def test_empty_tree(self):
        self.assertEqual(max_height(None), 0)

    def test_single_node_tree(self):
        node1 = Node(1)
        self.assertEqual(max_height(node1), 1)

    def test_left_taller_tree(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node1.left = node2
        node1.right = node3
        node2.left = node4
        self.assertEqual(max_height(node1), 3)

    def test_right_taller_tree(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node1.left = node2
        node3.right = node4
        node3.left = node5
        self.assertEqual(max_height(node1), 4)

    def test_unbalanced_tree(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node1.left = node2
        node2.left = node3
        node2.right = node4
        node1.right = node5
        node5.right = node6
        self.assertEqual(max_height(node1), 5)
