import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(min_val([]))

    def test_all_non_ints(self):
        self.assertIsNone(min_val([1.5, 'str', 3.14]))

    def test_all_negative_ints(self):
        self.assertEqual(min_val([-5, -3, -1]), -5)

    def test_all_positive_ints(self):
        self.assertEqual(min_val([1, 3, 5]), 1)

    def test_mixed_ints_and_non_ints(self):
        self.assertIsNone(min_val([1, 'str', 3]))

    def test_mixed_ints_and_floats(self):
        self.assertEqual(min_val([1.0, 2.0, 3]), 1.0)
