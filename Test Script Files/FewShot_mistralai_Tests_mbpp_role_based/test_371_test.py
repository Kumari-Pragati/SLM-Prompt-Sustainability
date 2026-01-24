import unittest
from mbpp_371_code import smallest_missing

class TestSmallestMissing(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(smallest_missing([], 0, len(smallest_missing([0])) - 1))

    def test_single_element(self):
        self.assertEqual(smallest_missing([1], 0, len(smallest_missing([1])) - 1), 2)

    def test_consecutive_elements(self):
        self.assertEqual(smallest_missing([1, 2, 3], 0, len(smallest_missing([1, 2, 3])) - 1), 4)

    def test_missing_element_in_middle(self):
        self.assertEqual(smallest_missing([1, 2, 4, 5], 0, len(smallest_missing([1, 2, 4, 5])) - 1), 3)

    def test_missing_element_at_beginning(self):
        self.assertEqual(smallest_missing([4, 1, 2, 5], 0, len(smallest_missing([4, 1, 2, 5])) - 1), 0)

    def test_missing_element_at_end(self):
        self.assertEqual(smallest_missing([1, 2, 5], 0, len(smallest_missing([1, 2, 5])) - 1), 3)

    def test_missing_element_in_middle_with_duplicates(self):
        self.assertEqual(smallest_missing([1, 1, 3, 5], 0, len(smallest_missing([1, 1, 3, 5])) - 1), 2)

    def test_left_element_greater_than_right_element(self):
        self.assertIsNone(smallest_missing([1, 2, 3], len(smallest_missing([1, 2, 3])) - 1, 0))
