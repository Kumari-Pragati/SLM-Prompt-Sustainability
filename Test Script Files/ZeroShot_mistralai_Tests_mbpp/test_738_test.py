import unittest
from mbpp_738_code import geometric_sum

class TestGeometricSum(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(geometric_sum(0), 1)

    def test_one(self):
        self.assertEqual(geometric_sum(1), 0.5)

    def test_negative(self):
        self.assertEqual(geometric_sum(-1), 0)

    def test_large_positive(self):
        self.assertAlmostEqual(geometric_sum(100), 0.0009765625, places=6)

    def test_large_negative(self):
        self.assertEqual(geometric_sum(-100), 0)
