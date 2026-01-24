import unittest
from592_code import sum_Of_product

class TestSumOfProduct(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(sum_Of_product(1), 1)
        self.assertEqual(sum_Of_product(2), 2)
        self.assertEqual(sum_Of_product(3), 5)
        self.assertEqual(sum_Of_product(4), 14)
        self.assertEqual(sum_Of_product(5), 42)

    def test_zero(self):
        self.assertEqual(sum_Of_product(0), 0)

    def test_negative_integer(self):
        self.assertRaises(ValueError, sum_Of_product, -1)
        self.assertRaises(ValueError, sum_Of_product, -2)

    def test_floating_point(self):
        self.assertRaises(TypeError, sum_Of_product, 2.5)
