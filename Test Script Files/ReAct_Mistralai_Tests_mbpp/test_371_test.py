import unittest
from mbpp_371_code import smallest_missing

class TestSmallestMissing(unittest.TestCase):

    def test_empty_list(self):
        self.assertIs(smallest_missing([], 0, len([0]) - 1), 0)

    def test_single_element(self):
        self.assertIs(smallest_missing([1], 0, len([1]) - 1), 2)

    def test_consecutive_elements(self):
        self.assertIs(smallest_missing([1, 2, 3], 0, len([1, 2, 3]) - 1), 4)

    def test_missing_element_in_middle(self):
        self.assertIs(smallest_missing([1, 2, 4, 5], 0, len([1, 2, 4, 5]) - 1), 3)

    def test_missing_element_at_beginning(self):
        self.assertIs(smallest_missing([4, 1, 2, 5], 0, len([4, 1, 2, 5]) - 1), 0)

    def test_missing_element_at_end(self):
        self.assertIs(smallest_missing([1, 2, 5], 0, len([1, 2, 5]) - 1), 3)

    def test_missing_element_in_reverse_order(self):
        self.assertIs(smallest_missing([5, 4, 3, 2, 1], 0, len([5, 4, 3, 2, 1]) - 1), 0)

    def test_left_element_greater_than_right_element(self):
        self.assertIs(smallest_missing([1, 2, 3], 4, 0), 4)

    def test_right_element_less_than_left_element(self):
        self.assertIs(smallest_missing([1, 2, 3], len([1, 2, 3]) - 1, -1), -1)

    def test_invalid_left_element(self):
        with self.assertRaises(IndexError):
            smallest_missing([1, 2, 3], -1, len([1, 2, 3]) - 1)

    def test_invalid_right_element(self):
        with self.assertRaises(IndexError):
            smallest_missing([1, 2, 3], len([1, 2, 3]), len([1, 2, 3]) + 1)
