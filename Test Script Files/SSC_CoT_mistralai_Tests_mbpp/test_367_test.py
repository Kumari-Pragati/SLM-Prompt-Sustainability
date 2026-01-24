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
        node6 = Node(6)
        node1.left = node2
        node1.right = node3
        node3.left = node4
        node3.right = node5
        node4.left = node6
        self.assertTrue(is_tree_balanced(node1))

    def test_left_heavier_tree(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)
        node1.left = node2
        node1.right = node3
        node3.left = node4
        node3.right = node5
        node4.left = node6
        node4.right = node7
        self.assertFalse(is_tree_balanced(node1))

    def test_right_heavier_tree(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)
        node1.left = node2
        node3.left = node4
        node3.right = node5
        node1.right = node3
        node4.left = node6
        node5.right = node7
        self.assertFalse(is_tree_balanced(node1))
