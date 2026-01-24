import unittest
from mbpp_738_code import geometric_sum

class TestGeometricSum(unittest.TestCase):

    def test_positive_integer(self):
        """Test sum for positive integers"""
        for n in range(1, 6):
            self.assertAlmostEqual(geometric_sum(n), (1 / (2 ** n)) + geometric_sum(n - 1))

    def test_zero(self):
        """Test sum for zero"""
        self.assertEqual(geometric_sum(0), 1)

    def test_negative_integer(self):
        """Test sum for negative integers"""
        self.assertEqual(geometric_sum(-1), 0)

    def test_large_integer(self):
        """Test sum for large integers"""
        self.assertAlmostEqual(geometric_sum(100), sum([1 / (2 ** i) for i in range(101)]))

    def test_float_input(self):
        """Test sum for float input"""
        self.assertAlmostEqual(geometric_sum(2.5), 1 / (2 ** 2) + geometric_sum(2.5 - 1))
