import unittest
from mbpp_927_code import max_height

class TestMaxHeight(unittest.TestCase):

    def test_empty_tree(self):
        """Test max_height on an empty tree"""
        self.assertEqual(max_height(None), 0)

    def test_single_node_tree(self):
        """Test max_height on a tree with a single node"""
        node = Node(1)
        self.assertEqual(max_height(node), 1)

    def test_unbalanced_tree(self):
        """Test max_height on an unbalanced tree"""
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

    def test_balanced_tree(self):
        """Test max_height on a balanced tree"""
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)

        node1.left = node2
        node1.right = node3
        node2.left = node4
        node3.left = node5

        self.assertEqual(max_height(node1), 4)

    def test_null_node_left(self):
        """Test max_height on a tree with a null left child"""
        node = Node(1)
        node.left = None
        node.right = Node(2)
        self.assertEqual(max_height(node), 2)

    def test_null_node_right(self):
        """Test max_height on a tree with a null right child"""
        node = Node(1)
        node.left = Node(2)
        node.right = None
        self.assertEqual(max_height(node), 2)
