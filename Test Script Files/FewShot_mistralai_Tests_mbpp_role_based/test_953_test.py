import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(subset([], 0), 0)

    def test_single_element(self):
        self.assertEqual(subset([1], 1), 1)

    def test_single_duplicate(self):
        self.assertEqual(subset([1, 1], 1), 1)

    def test_multiple_elements(self):
        self.assertEqual(subset([1, 2, 3], 3), 1)

    def test_multiple_duplicates(self):
        self.assertEqual(subset([1, 1, 2, 2, 3], 3), 2)

    def test_negative_n(self):
        self.assertRaises(ValueError, subset, [1, 2, 3], -1)

    def test_empty_n(self):
        self.assertRaises(ValueError, subset, [1, 2, 3], 0)

    def test_non_iterable_ar(self):
        self.assertRaises(TypeError, subset, "string", 3)
