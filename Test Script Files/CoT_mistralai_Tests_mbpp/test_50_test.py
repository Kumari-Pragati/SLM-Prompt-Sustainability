import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(min_length_list([]))

    def test_single_element_list(self):
        self.assertEqual(min_length_list([1]), (1, [1]))

    def test_multiple_elements_same_length(self):
        self.assertEqual(min_length_list([[1, 2], [3, 4], [5, 6]]), (2, [[1, 2], [3, 4], [5, 6]]))

    def test_multiple_elements_different_lengths(self):
        self.assertEqual(min_length_list([[1], [1, 2], [1, 2, 3]]), ((1,), [ [1], [1, 2], [1, 2, 3]]))

    def test_min_length_with_duplicates(self):
        self.assertEqual(min_length_list([[1], [1, 2], [1, 2, 3], [1, 2, 3]]), ((1,), [ [1], [1, 2], [1, 2, 3], [1, 2, 3]]))

    def test_min_length_with_empty_elements(self):
        self.assertEqual(min_length_list([[], [1], [1, 2], [1, 2, 3]]), (0, []))

    def test_min_length_with_non_list_input(self):
        self.assertRaises(TypeError, min_length_list, "not a list")
