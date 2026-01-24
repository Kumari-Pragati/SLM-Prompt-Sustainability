import unittest
from mbpp_927_code import max_height

class TestMaxHeight(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_input(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        self.assertEqual(max_height(node), 2)

    # Test for edge and boundary conditions
    def test_empty_input(self):
        self.assertEqual(max_height(None), 0)

    def test_single_node_input(self):
        node = Node(1)
        self.assertEqual(max_height(node), 1)

    # Test for more complex or corner cases
    def test_complex_input(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        node.left.left = Node(4)
        node.left.right = Node(5)
        node.right.left = Node(6)
        node.right.right = Node(7)
        self.assertEqual(max_height(node), 4)
