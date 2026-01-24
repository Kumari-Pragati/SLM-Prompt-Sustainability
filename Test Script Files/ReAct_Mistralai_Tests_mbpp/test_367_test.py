import unittest
from mbpp_367_code import MagicMock
from unittest.mock import patch

class TestIsTreeBalanced(unittest.TestCase):

    def setUp(self):
        self.node = Node(1)
        self.unbalanced_node = Node(1)
        self.unbalanced_node.left = Node(2)
        self.unbalanced_node.left.left = Node(3)
        self.unbalanced_node.right = Node(4)
        self.unbalanced_node.right.right = Node(5)
        self.balanced_node = Node(1)
        self.balanced_node.left = Node(2)
        self.balanced_node.right = Node(3)
        self.empty_tree = None

    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(self.empty_tree))

    def test_single_node(self):
        self.assertTrue(is_tree_balanced(self.node))

    def test_unbalanced_tree(self):
        self.assertFalse(is_tree_balanced(self.unbalanced_node))

    def test_balanced_tree(self):
        self.assertTrue(is_tree_balanced(self.balanced_node))

    @patch('module_name.get_height')
    def test_get_height_exception(self, mock_get_height):
        mock_get_height.side_effect = Exception("Mock exception")
        self.assertRaises(Exception, is_tree_balanced, self.node)
