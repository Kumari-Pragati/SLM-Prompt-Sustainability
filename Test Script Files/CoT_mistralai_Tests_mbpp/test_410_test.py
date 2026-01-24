import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(min_val([]))

    def test_all_non_ints(self):
        self.assertIsNone(min_val(['a', 'b', 'c']))

    def test_all_zero(self):
        self.assertEqual(min_val([0, 0, 0]), 0)

    def test_all_positive(self):
        self.assertEqual(min_val([1, 2, 3]), 1)

    def test_all_negative(self):
        self.assertEqual(min_val([-1, -2, -3]), -1)

    def test_mixed_ints_and_non_ints(self):
        self.assertIsNone(min_val(['a', 1, 'b', 2]))

    def test_mixed_ints_and_floats(self):
        self.assertEqual(min_val([1.0, 2.0, 3, 4.0]), 1.0)

    def test_mixed_floats_and_ints(self):
        self.assertEqual(min_val([1, 2.0, 3.0, 4]), 1)

    def test_mixed_ints_and_complex(self):
        self.assertIsNone(min_val([1j, 1, 2j]))

    def test_mixed_complex_and_ints(self):
        self.assertIsNone(min_val([1, 1j, 2, 3j]))
