import unittest
from mbpp_34_code import find_missing

class TestFindMissing(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_missing([], 1), -1)

    def test_single_element(self):
        self.assertEqual(find_missing([1], 1), -1)
        self.assertEqual(find_missing([10], 10), -1)

    def test_consecutive_elements(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 5], 5), -1)
        self.assertEqual(find_missing([6, 7, 8, 9, 10], 5), 6)

    def test_missing_element_in_middle(self):
        self.assertEqual(find_missing([1, 2, 4, 5], 3), 3)

    def test_missing_element_at_beginning(self):
        self.assertEqual(find_missing([4, 5, 6, 7, 8], 1), 1)

    def test_missing_element_at_end(self):
        self.assertEqual(find_missing([1, 2, 3, 5, 6], 4), 4)

    def test_multiple_missing_elements(self):
        self.assertEqual(find_missing([1, 2, 4, 6, 7], 3, 5), 3)
        self.assertEqual(find_missing([1, 2, 4, 6, 7], 3, 5, 8), 5)
