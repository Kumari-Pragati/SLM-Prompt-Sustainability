import unittest
from mbpp_137_code import zero_count

class TestZeroCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(zero_count([1, 0, 2, 0, 3]), 0.4, places=2)

    def test_empty_list(self):
        self.assertEqual(zero_count([]), 0.0)

    def test_all_zeros(self):
        self.assertEqual(zero_count([0, 0, 0, 0]), 1.0)

    def test_all_non_zeros(self):
        self.assertEqual(zero_count([1, 2, 3, 4]), 0.0)

    def test_single_zero(self):
        self.assertEqual(zero_count([0]), 1.0)

    def test_large_list(self):
        self.assertAlmostEqual(zero_count([0]*10000 + [1, 2, 3]), 0.03, places=2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            zero_count("not a list")
