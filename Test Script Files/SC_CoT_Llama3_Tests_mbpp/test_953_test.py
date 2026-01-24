import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(subset([1, 2, 2, 3, 3, 3], 6), 3)

    def test_edge(self):
        self.assertEqual(subset([1, 1, 1, 2, 2, 2, 3, 3, 3], 9), 3)

    def test_empty(self):
        self.assertEqual(subset([], 0), 0)

    def test_single(self):
        self.assertEqual(subset([1], 1), 1)

    def test_all_equal(self):
        self.assertEqual(subset([1, 1, 1, 1, 1, 1], 6), 6)

    def test_no_duplicates(self):
        self.assertEqual(subset([1, 2, 3, 4, 5], 5), 1)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            subset('abc', 5)

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            subset([1, 2, 3], 'a')
