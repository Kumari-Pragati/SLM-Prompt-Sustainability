import unittest
from mbpp_712_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 4, 4, 4, 5, 5, 5]), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        self.assertEqual(remove_duplicate([]), [])

    def test_single_element(self):
        self.assertEqual(remove_duplicate([1]), [1])

    def test_duplicate_in_middle(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3]), [1, 2, 3])

    def test_duplicate_at_start(self):
        self.assertEqual(remove_duplicate([2, 2, 3, 4]), [2, 3, 4])

    def test_duplicate_at_end(self):
        self.assertEqual(remove_duplicate([1, 2, 3, 3]), [1, 2, 3])

    def test_duplicate_in_all_positions(self):
        self.assertEqual(remove_duplicate([2, 2, 2, 2]), [2])

    def test_negative_numbers(self):
        self.assertEqual(remove_duplicate([-1, -1, 0, 0, 1, 1]), [-1, 0, 1])

    def test_large_numbers(self):
        self.assertEqual(remove_duplicate([1000, 1000, 2000, 2000]), [1000, 2000])
