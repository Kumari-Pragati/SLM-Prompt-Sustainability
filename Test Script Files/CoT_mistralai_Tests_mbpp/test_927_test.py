import unittest
from mbpp_927_code import max_height

class TestMaxHeight(unittest.TestCase):

    def test_empty_tree(self):
        self.assertEqual(max_height(None), 0)

    def test_single_node_tree(self):
        node = Node(1)
        self.assertEqual(max_height(node), 1)

    def test_balanced_tree(self):
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

    def test_unbalanced_tree(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)
        node8 = Node(8)
        node9 = Node(9)
        node10 = Node(10)
        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = node5
        node3.left = node6
        node3.right = node7
        node4.left = node8
        node5.right = node9
        node6.left = node10
        self.assertEqual(max_height(node1), 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_height(123)
