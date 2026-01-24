import unittest
from mbpp_371_code import smallest_missing

class TestSmallestMissing(unittest.TestCase):

    def test_empty_list(self):
        self.assertIs(smallest_missing([], 0, len(range(0)) - 1), None)

    def test_single_element(self):
        self.assertEqual(smallest_missing([1], 0, len(range(0)) - 1), None)

    def test_consecutive_elements(self):
        self.assertEqual(smallest_missing(list(range(1, 6)), 0, 5), 6)
        self.assertEqual(smallest_missing(list(range(1, 6)), 6, len(range(6)) - 1), None)

    def test_missing_element_in_middle(self):
        self.assertEqual(smallest_missing(list(range(1, 6)) + [0], 0, len(range(6)) - 1), 1)

    def test_missing_element_at_beginning(self):
        self.assertEqual(smallest_missing(list(range(2, 6)) + [0, 1], 0, len(range(6)) - 1), 0)

    def test_missing_element_at_end(self):
        self.assertEqual(smallest_missing(list(range(1, 6)) + [7], 0, len(range(7)) - 1), 6)

    def test_missing_element_in_reverse_order(self):
        self.assertEqual(smallest_missing(list(reversed(range(1, 6))) + [0], 0, len(range(6)) - 1), 1)

    def test_invalid_input_left_greater_right(self):
        with self.assertRaises(ValueError):
            smallest_missing([1], len(range(1)) - 1, 0)

    def test_invalid_input_negative_index(self):
        with self.assertRaises(IndexError):
            smallest_missing([1], 0, -1)
