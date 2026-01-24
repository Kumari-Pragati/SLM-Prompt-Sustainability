import unittest
from mbpp_346_code import zigzag

class TestZigzag(unittest.TestCase):

    def test_zero_n_zero_k(self):
        self.assertEqual(zigzag(0, 0), 1)

    def test_zero_n_non_zero_k(self):
        self.assertEqual(zigzag(0, 1), 0)

    def test_non_zero_n_zero_k(self):
        self.assertEqual(zigzag(1, 0), 0)

    def test_typical_cases(self):
        self.assertEqual(zigzag(2, 1), 1)
        self.assertEqual(zigzag(3, 2), 2)
        self.assertEqual(zigzag(4, 1), 4)

    def test_boundary_conditions(self):
        self.assertEqual(zigzag(5, 5), 1)
        self.assertEqual(zigzag(6, 6), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(Exception):
            zigzag(-1, 1)
        with self.assertRaises(Exception):
            zigzag(1, -1)
        with self.assertRaises(Exception):
            zigzag(-1, -1)
