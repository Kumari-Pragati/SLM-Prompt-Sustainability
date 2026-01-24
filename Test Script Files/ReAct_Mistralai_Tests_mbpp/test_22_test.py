import unittest
from mbpp_22_code import find_first_duplicate

class TestFindFirstDuplicate(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_first_duplicate([]), -1)

    def test_single_element_list(self):
        self.assertEqual(find_first_duplicate([1]), -1)

    def test_no_duplicates(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 4, 5]), -1)

    def test_duplicate_at_beginning(self):
        self.assertEqual(find_first_duplicate([2, 1, 2, 3, 4]), 2)

    def test_duplicate_in_middle(self):
        self.assertEqual(find_first_duplicate([1, 2, 2, 3, 4]), 2)

    def test_duplicate_at_end(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 3, 4]), 3)

    def test_duplicate_with_only_duplicates(self):
        self.assertEqual(find_first_duplicate([2, 2, 2, 2]), 2)

    def test_negative_numbers(self):
        self.assertEqual(find_first_duplicate([-1, -2, -2, -3]), -2)

    def test_large_numbers(self):
        self.assertEqual(find_first_duplicate([1000000001, 1000000001, 1000000002]), 1000000001)
