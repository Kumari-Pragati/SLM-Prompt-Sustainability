import unittest
from mbpp_927_code import Node, max_height

class TestMaxHeight(unittest.TestCase):

    def setUp(self):
        self.node1 = Node(1)
        self.node2 = Node(2)
        self.node3 = Node(3)
        self.node4 = Node(4)
        self.node5 = Node(5)
        self.node6 = Node(6)
        self.node7 = Node(7)

        self.tree = Node(0)
        self.tree.left = self.node1
        self.tree.right = self.tree.left
        self.tree.left.left = self.node2
        self.tree.left.right = self.node3
        self.tree.left.left.left = self.node4
        self.tree.left.left.right = self.node5
        self.tree.left.right.left = self.node6
        self.tree.left.right.right = self.node7

    def test_empty_tree(self):
        self.assertEqual(max_height(None), 0)

    def test_single_node_tree(self):
        self.assertEqual(max_height(self.node1), 1)
        self.assertEqual(max_height(self.tree), 2)

    def test_balanced_tree(self):
        self.assertEqual(max_height(self.tree), 4)

    def test_unbalanced_left_tree(self):
        self.assertEqual(max_height(self.node1.left), 1)
        self.assertEqual(max_height(self.node1), 2)

    def test_unbalanced_right_tree(self):
        self.node1.right = None
        self.node2.right = None
        self.node3.right = None
        self.node4.right = None
        self.node5.right = None
        self.node6.right = None
        self.node7.right = None
        self.node1.left = None
        self.node2.left = None
        self.node3.left = None
        self.node4.left = None
        self.node5.left = None
        self.node6.left = None

        self.node1.left = self.node2
        self.node2.left = self.node3
        self.node3.left = self.node4
        self.node4.left = self.node5
        self.node5.left = self.node6
        self.node6.left = self.node7

        self.assertEqual(max_height(self.node1), 6)
