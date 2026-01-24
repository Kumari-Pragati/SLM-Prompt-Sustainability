import unittest
from mbpp_367_code import is_tree_balanced

class TestIsTreeBalanced(unittest.TestCase):

    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))

    def test_single_node_tree(self):
        node = Node(1)
        self.assertTrue(is_tree_balanced(node))

    def test_unbalanced_tree(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)

        node1.left = node2
        node1.right = node3
        node3.left = node4
        node3.right = node5

        self.assertFalse(is_tree_balanced(node1))

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

        self.assertTrue(is_tree_balanced(node1))

    def test_balanced_tree_with_empty_subtree(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)

        node1.left = node2
        node1.right = node3
        node2.left = None
        node3.right = node5

        self.assertTrue(is_tree_balanced(node1))
