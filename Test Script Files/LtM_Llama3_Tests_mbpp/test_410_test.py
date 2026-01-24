import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(min_val([1, 2, 3]), 1)
        self.assertEqual(min_val([5, 2, 8]), 2)
        self.assertEqual(min_val([-1, 0, 1]), -1)

    def test_empty_list(self):
        self.assertIsNone(min_val([]))

    def test_non_integer_values(self):
        self.assertRaises(TypeError, min_val, [1, 2, 'a', 4])

    def test_single_integer_value(self):
        self.assertEqual(min_val([5]), 5)

    def test_multiple_integer_values(self):
        self.assertEqual(min_val([1, 2, 3, 4, 5]), 1)

    def test_negative_integer_values(self):
        self.assertEqual(min_val([-1, 0, 1]), -1)

    def test_positive_integer_values(self):
        self.assertEqual(min_val([1, 2, 3, 4, 5]), 1)
