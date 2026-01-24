import unittest
from mbpp_34_code import find_missing

class TestFindMissing(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_missing([], 1), -1)

    def test_single_element_list(self):
        self.assertEqual(find_missing([1], 1), -1)
        self.assertEqual(find_missing([1], 2), 2)

    def test_consecutive_list(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 5], 5), -1)

    def test_missing_element_in_middle(self):
        self.assertEqual(find_missing([1, 2, 3, 5, 6], 4), 4)

    def test_missing_element_at_beginning(self):
        self.assertEqual(find_missing([2, 3, 4, 5, 6], 1), 1)

    def test_missing_element_at_end(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 7], 5), 6)

    def test_duplicate_elements(self):
        self.assertEqual(find_missing([1, 1, 2, 3], 4), -1)

    def test_out_of_range_input(self):
        self.assertEqual(find_missing([1, 2, 3], 4), -1)
        self.assertEqual(find_missing([1, 2, 3], 0), -1)
