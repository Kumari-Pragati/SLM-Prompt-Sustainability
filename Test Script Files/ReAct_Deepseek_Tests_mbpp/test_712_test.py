import unittest
from mbpp_712_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 4, 4, 4, 5, 5, 5]), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        self.assertEqual(remove_duplicate([]), [])

    def test_single_element(self):
        self.assertEqual(remove_duplicate([1]), [1])

    def test_duplicate_elements(self):
        self.assertEqual(remove_duplicate([1, 1, 1, 1]), [1])

    def test_sorted_list(self):
        self.assertEqual(remove_duplicate([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(remove_duplicate([5, 4, 3, 2, 1]), [5, 4, 3, 2, 1])

    def test_negative_numbers(self):
        self.assertEqual(remove_duplicate([-5, -4, -3, -2, -1, -1]), [-5, -4, -3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(remove_duplicate([1, -1, 2, -2, 3, -3]), [1, -1, 2, -2, 3, -3])
