import unittest
from mbpp_378_code import move_first

class TestMoveFirst(unittest.TestCase):

    def test_empty_list(self):
        """Test moving elements in an empty list"""
        self.assertEqual(move_first([]), [])

    def test_single_element_list(self):
        """Test moving elements in a single-element list"""
        self.assertEqual(move_first([1]), [1])

    def test_multiple_elements_list(self):
        """Test moving elements in a multiple-element list"""
        self.assertEqual(move_first([1, 2, 3]), [3, 1, 2])

    def test_list_with_duplicates(self):
        """Test moving elements in a list with duplicates"""
        self.assertEqual(move_first([1, 2, 1, 3]), [3, 1, 2, 1])

    def test_list_with_negative_index(self):
        """Test moving elements with a negative index"""
        self.assertEqual(move_first([1, 2, 3]), [3, 1, 2])

    def test_list_with_non_list_input(self):
        """Test moving elements with non-list input"""
        with self.assertRaises(TypeError):
            move_first("not a list")
