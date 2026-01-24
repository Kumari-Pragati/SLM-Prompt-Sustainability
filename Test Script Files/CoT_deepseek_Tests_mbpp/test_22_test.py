import unittest
from mbpp_22_code import find_first_duplicate

class TestFindFirstDuplicate(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 2]), 2)

    def test_no_duplicate(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 4]), -1)

    def test_empty_list(self):
        self.assertEqual(find_first_duplicate([]), -1)

    def test_duplicate_at_beginning(self):
        self.assertEqual(find_first_duplicate([2, 1, 2]), 2)

    def test_duplicate_at_end(self):
        self.assertEqual(find_first_duplicate([1, 2, 2]), 2)

    def test_duplicate_in_middle(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 2, 4]), 2)

    def test_duplicate_with_negative_numbers(self):
        self.assertEqual(find_first_duplicate([1, -2, 3, -2]), -2)

    def test_duplicate_with_zero(self):
        self.assertEqual(find_first_duplicate([0, 1, 2, 0]), 0)

    def test_duplicate_with_large_numbers(self):
        self.assertEqual(find_first_duplicate([1000000, 2000000, 1000000]), 1000000)
