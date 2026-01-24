import unittest
from mbpp_367_code import is_tree_balanced

class TestIsTreeBalanced(unittest.TestCase):

    def setUp(self):
        self.node1 = Node(1)
        self.node2 = Node(2)
        self.node3 = Node(3)
        self.node4 = Node(4)
        self.node5 = Node(5)

    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))

    def test_single_node_tree(self):
        self.node1.left = None
        self.node1.right = None
        self.assertTrue(is_tree_balanced(self.node1))

    def test_balanced_tree(self):
        self.node1.left = self.node2
        self.node1.right = self.node3
        self.node2.left = self.node4
        self.node2.right = self.node5
        self.assertTrue(is_tree_balanced(self.node1))

    def test_unbalanced_tree(self):
        self.node1.left = self.node2
        self.node1.right = self.node3
        self.node2.left = self.node4
        self.assertFalse(is_tree_balanced(self.node1))

    def test_tree_with_one_node_left(self):
        self.node1.left = self.node2
        self.assertFalse(is_tree_balanced(self.node1))

    def test_tree_with_one_node_right(self):
        self.node1.right = self.node2
        self.assertFalse(is_tree_balanced(self.node1))
