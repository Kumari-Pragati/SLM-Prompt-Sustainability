import unittest
from mbpp_471_code import find_remainder

class TestFindRemainder(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 4), 1)

    def test_edge_case_n_zero(self):
        with self.assertRaises(ZeroDivisionError):
            find_remainder([1, 2, 3], 3, 0)

    def test_edge_case_n_one(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 1), 1)

    def test_edge_case_lens_zero(self):
        with self.assertRaises(ZeroDivisionError):
            find_remainder([], 0, 4)

    def test_edge_case_lens_one(self):
        self.assertEqual(find_remainder([1], 1, 4), 1)

    def test_edge_case_lens_negative(self):
        with self.assertRaises(ValueError):
            find_remainder([1, 2, 3], -1, 4)

    def test_edge_case_n_negative(self):
        with self.assertRaises(ValueError):
            find_remainder([1, 2, 3], 3, -4)

    def test_edge_case_lens_and_n_negative(self):
        with self.assertRaises(ValueError):
            find_remainder([1, 2, 3], -1, -4)

    def test_edge_case_lens_zero_and_n_negative(self):
        with self.assertRaises(ValueError):
            find_remainder([], -1, -4)

    def test_edge_case_lens_one_and_n_negative(self):
        with self.assertRaises(ValueError):
            find_remainder([1], -1, -4)
