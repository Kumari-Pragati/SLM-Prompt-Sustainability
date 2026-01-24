import unittest
from702_code import removals

class TestRemovals(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(removals([], 0, 0), 0)

    def test_single_element(self):
        self.assertEqual(removals([1], 1, 0), 0)
        self.assertEqual(removals([1], 1, 1), 0)

    def test_sorted_list(self):
        self.assertEqual(removals([1, 2, 3], 3, 1), 2)
        self.assertEqual(removals([1, 2, 3], 3, 2), 1)

    def test_unsorted_list(self):
        self.assertEqual(removals([3, 1, 2], 3, 1), 2)
        self.assertEqual(removals([3, 1, 2], 3, 2), 0)

    def test_negative_key(self):
        self.assertEqual(removals([1, 2, 3], 3, -1), 2)

    def test_key_greater_than_all_elements(self):
        self.assertEqual(removals([1, 2, 3], 3, 4), 3)

    def test_invalid_input_k_greater_than_n(self):
        self.assertRaises(ValueError, removals, [1, 2, 3], 3, 4)

    def test_invalid_input_negative_n(self):
        self.assertRaises(ValueError, removals, [1, 2, 3], -1, 1)
