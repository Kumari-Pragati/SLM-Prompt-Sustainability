import unittest
from mbpp_371_code import smallest_missing

class TestSmallestMissing(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(smallest_missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 9), 10)

    def test_edge_left_greater_right(self):
        self.assertEqual(smallest_missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 9), 10)

    def test_edge_right_greater_left(self):
        self.assertEqual(smallest_missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 0), 0)

    def test_edge_equal(self):
        self.assertEqual(smallest_missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 0), 1)

    def test_invalid_input_left_greater_right(self):
        with self.assertRaises(ValueError):
            smallest_missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 5)

    def test_invalid_input_right_greater_left(self):
        with self.assertRaises(ValueError):
            smallest_missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 10)
