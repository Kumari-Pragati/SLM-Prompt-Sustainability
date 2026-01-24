import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):
    def test_min_length_and_min_list_with_same_length_list(self):
        self.assertEqual(min_length_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), (3, [1, 2, 3]))

    def test_min_length_and_min_list_with_different_length_list(self):
        self.assertEqual(min_length_list([[1, 2, 3], [4], [7, 8, 9]])), (2, [4])

    def test_min_length_and_min_list_with_empty_list(self):
        self.assertEqual(min_length_list([]), (0, []))

    def test_min_length_and_min_list_with_single_element_list(self):
        self.assertEqual(min_length_list([[1]]), (1, [1]))

    def test_min_length_and_min_list_with_negative_numbers(self):
        self.assertEqual(min_length_list([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), (3, [-1, -2, -3]))
