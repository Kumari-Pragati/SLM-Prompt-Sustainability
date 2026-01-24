import unittest
from mbpp_517_code import largest_pos

class TestLargestPos(unittest.TestCase):

    def test_empty_list(self):
        self.assertRaises(IndexError, largest_pos, [])

    def test_single_element_list(self):
        self.assertEqual(largest_pos([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(largest_pos([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers_list(self):
        self.assertEqual(largest_pos([-1, -2, -3, -4, -5]), -1)

    def test_mixed_positive_and_negative_numbers_list(self):
        self.assertEqual(largest_pos([1, -2, 3, -4, 5]), 5)

    def test_duplicate_elements_list(self):
        self.assertEqual(largest_pos([1, 1, 2, 3, 4, 5]), 5)

    def test_list_with_zero(self):
        self.assertEqual(largest_pos([0, 1, 2, 3, 4, 5]), 5)

    def test_list_with_float(self):
        self.assertEqual(largest_pos([1.1, 2.2, 3.3, 4.4, 5.5]), 5.5)
