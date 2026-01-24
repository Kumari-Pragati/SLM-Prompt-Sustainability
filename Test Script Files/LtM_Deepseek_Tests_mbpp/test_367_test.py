import unittest
from mbpp_367_code import is_tree_balanced

class TestIsTreeBalanced(unittest.TestCase):

    # Test for typical balanced tree
    def test_typical_balanced_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertTrue(is_tree_balanced(root))

    # Test for tree with one node
    def test_single_node_tree(self):
        root = Node(1)
        self.assertTrue(is_tree_balanced(root))

    # Test for tree with two nodes
    def test_two_nodes_tree(self):
        root = Node(1)
        root.left = Node(2)
        self.assertTrue(is_tree_balanced(root))

    # Test for tree with right heavy nodes
    def test_right_heavy_tree(self):
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)
        self.assertFalse(is_tree_balanced(root))

    # Test for tree with left heavy nodes
    def test_left_heavy_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        self.assertFalse(is_tree_balanced(root))

    # Test for empty tree
    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))
