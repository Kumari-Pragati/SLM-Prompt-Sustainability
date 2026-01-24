import unittest
from mbpp_367_code import Node, is_tree_balanced

class TestIsTreeBalanced(unittest.TestCase):

    def setUp(self):
        self.node1 = Node(1)
        self.node2 = Node(2)
        self.node3 = Node(3)
        self.node4 = Node(4)
        self.node5 = Node(5)
        self.node6 = Node(6)
        self.node7 = Node(7)
        self.node8 = Node(8)
        self.node9 = Node(9)
        self.node10 = Node(10)

        self.tree1 = Node(1)
        self.tree1.left = self.node2
        self.tree1.right = self.node3

        self.tree2 = Node(2)
        self.tree2.left = self.node1
        self.tree2.right = self.tree1

        self.tree3 = Node(3)
        self.tree3.left = self.node2
        self.tree3.right = Node(4)
        self.tree3.right.right = self.node5

        self.tree4 = Node(4)
        self.tree4.left = self.node2
        self.tree4.right = Node(5)
        self.tree4.right.right = Node(6)
        self.tree4.right.right.right = self.node7
        self.tree4.left.left = Node(3)
        self.tree4.left.right = Node(8)

    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))

    def test_single_node_tree(self):
        self.assertTrue(is_tree_balanced(self.node1))

    def test_unbalanced_tree(self):
        self.assertFalse(is_tree_balanced(self.tree3))

    def test_balanced_tree(self):
        self.assertTrue(is_tree_balanced(self.tree2))

    def test_balanced_but_not_perfect_tree(self):
        self.assertTrue(is_tree_balanced(self.tree1))

    def test_perfectly_balanced_tree(self):
        self.assertTrue(is_tree_balanced(self.tree4))
