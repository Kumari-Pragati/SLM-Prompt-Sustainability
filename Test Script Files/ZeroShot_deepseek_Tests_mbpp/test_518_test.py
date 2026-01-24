import unittest
from mbpp_518_code import sqrt_root

class TestSqrtRoot(unittest.TestCase):

    def test_sqrt_root_positive_number(self):
        self.assertAlmostEqual(sqrt_root(4), 2.0)

    def test_sqrt_root_zero(self):
        self.assertEqual(sqrt_root(0), 0)

    def test_sqrt_root_negative_number(self):
        with self.assertRaises(ValueError):
            sqrt_root(-4)
