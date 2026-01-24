import unittest
from mbpp_22_code import find_first_duplicate

class TestFindFirstDuplicate(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 2]), 2)

    def test_no_duplicate(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 4]), -1)

    def test_empty_list(self):
        self.assertEqual(find_first_duplicate([]), -1)

    def test_single_element(self):
        self.assertEqual(find_first_duplicate([1]), -1)

    def test_duplicate_at_beginning(self):
        self.assertEqual(find_first_duplicate([2, 1, 3, 2]), 2)

    def test_duplicate_at_end(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 2]), 2)

    def test_duplicate_in_middle(self):
        self.assertEqual(find_first_duplicate([1, 2, 2, 3]), 2)

    def test_duplicate_with_same_value(self):
        self.assertEqual(find_first_duplicate([1, 1, 1, 1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(find_first_duplicate([-1, -2, -2]), -2)

    def test_large_numbers(self):
        self.assertEqual(find_first_duplicate([1000, 2000, 2000]), 2000)

    def test_duplicate_in_large_list(self):
        self.assertEqual(find_first_duplicate(list(range(1, 10000)) + [5000]), 5000)
