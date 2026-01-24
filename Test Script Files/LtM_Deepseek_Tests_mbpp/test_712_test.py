import unittest
from mbpp_712_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 4]), [1, 2, 3, 4])

    def test_empty_input(self):
        self.assertEqual(remove_duplicate([]), [])

    def test_duplicate_input(self):
        self.assertEqual(remove_duplicate([1, 1, 1, 1]), [1])

    def test_single_element_input(self):
        self.assertEqual(remove_duplicate([5]), [5])

    def test_sorted_input(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 4]), [1, 2, 3, 4])

    def test_unsorted_input(self):
        self.assertEqual(remove_duplicate([4, 2, 2, 3, 1]), [4, 2, 3, 1])

    def test_negative_numbers(self):
        self.assertEqual(remove_duplicate([-1, -2, -2, -3]), [-1, -2, -3])

    def test_mixed_numbers(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, -1]), [1, 2, 3, -1])
